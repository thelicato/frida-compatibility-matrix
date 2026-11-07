import unittest
from unittest.mock import Mock, call, patch

from scripts.parser import (
    GITHUB_RAW,
    GitHubRequestError,
    get_all_dependencies,
    get_structured_data,
    make_request,
)


class DependencyTests(unittest.TestCase):
    @patch("scripts.parser.get_github_headers", return_value={})
    @patch("scripts.parser.make_request")
    def test_modern_and_legacy_releases(self, request, headers):
        modern_setup = f"{GITHUB_RAW['tags']}/14.13.0/setup.py"
        modern_project = f"{GITHUB_RAW['tags']}/14.13.0/pyproject.toml"
        legacy_setup = f"{GITHUB_RAW['tags']}/14.11.0/setup.py"
        request.side_effect = [
            GitHubRequestError(404, b"404: Not Found", modern_setup),
            b'''[project]
dependencies = [
    "colorama >= 0.2.7, < 1.0.0",
    "frida >= 17.26.0, < 18.0.0",
]
[project.scripts]
frida = "frida_tools.repl:main"
''',
            b'''setup(install_requires=[
    "colorama >= 0.2.7, < 1.0.0",
    "frida >= 17.10.0, < 18.0.0",
])''',
        ]

        matrix = get_all_dependencies(["14.13.0", "14.11.0"])

        self.assertEqual(matrix, {
            "14.13.0": ">= 17.26.0, < 18.0.0",
            "14.11.0": ">= 17.10.0, < 18.0.0",
        })
        self.assertEqual(get_structured_data(matrix), {
            "14.13.0": {"gte": "17.26.0", "lt": "18.0.0"},
            "14.11.0": {"gte": "17.10.0", "lt": "18.0.0"},
        })
        self.assertEqual(request.call_args_list, [
            call(GITHUB_RAW["base"], modern_setup, {}),
            call(GITHUB_RAW["base"], modern_project, {}),
            call(GITHUB_RAW["base"], legacy_setup, {}),
        ])

    @patch("scripts.parser.get_github_headers", return_value={})
    @patch("scripts.parser.make_request")
    def test_legacy_single_quotes_and_compact_specifiers(self, request, headers):
        request.return_value = b"setup(install_requires=[\n    'frida>=12.0.0,<13.0.0',\n])"

        self.assertEqual(get_all_dependencies(["1.0.0"]), {
            "1.0.0": ">= 12.0.0, < 13.0.0",
        })

    @patch("scripts.parser.get_github_headers", return_value={})
    @patch("scripts.parser.make_request")
    def test_other_http_errors_do_not_trigger_fallback(self, request, headers):
        for status in (401, 403, 429, 500):
            with self.subTest(status=status):
                request.reset_mock()
                request.side_effect = GitHubRequestError(status, b"failed", "/setup.py")

                with self.assertRaisesRegex(Exception, f"tag 14.13.0.*status code {status}"):
                    get_all_dependencies(["14.13.0"])

                request.assert_called_once()

    @patch("scripts.parser.get_github_headers", return_value={})
    @patch("scripts.parser.make_request")
    def test_missing_or_invalid_metadata_is_not_silently_skipped(self, request, headers):
        for metadata in (
            GitHubRequestError(404, b"Not Found", "/pyproject.toml"),
            b"[project\n",
            b'[project]\ndependencies = ["frida-tools >= 14.0.0"]',
        ):
            with self.subTest(metadata=metadata):
                request.side_effect = [
                    GitHubRequestError(404, b"Not Found", "/setup.py"),
                    metadata,
                ]

                with self.assertRaisesRegex(Exception, "tag 14.13.0"):
                    get_all_dependencies(["14.13.0"])


class RequestTests(unittest.TestCase):
    @patch("scripts.parser.http.client.HTTPSConnection")
    def test_404_exposes_status_for_metadata_fallback(self, connection):
        response = Mock(status=404)
        response.read.return_value = b"404: Not Found"
        connection.return_value.getresponse.return_value = response

        with self.assertRaises(GitHubRequestError) as error:
            make_request("raw.githubusercontent.com", "/setup.py", {})

        self.assertEqual(error.exception.status, 404)
        self.assertIn("/setup.py", str(error.exception))
        connection.return_value.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
