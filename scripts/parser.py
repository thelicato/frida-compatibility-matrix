import os
import json
import http.client
import re
import tomllib

GITHUB_API = {
    'base': "api.github.com",
    'tags': "/repos/frida/frida-tools/tags"
}
GITHUB_RAW = {
    'base': "raw.githubusercontent.com",
    'tags': "/frida/frida-tools/refs/tags"
}

FRIDA_TOOLS_REPO = "frida/frida-tools"

class GitHubRequestError(Exception):
    """An unsuccessful GitHub response, including its HTTP status."""

    def __init__(self, status, data, url):
        self.status = status
        super().__init__(f"[-] ERROR: status code {status} - error {data.decode()} - url {url}")

def get_github_headers():
    """Returns GitHub authentication headers if a token is available."""
    github_token = os.getenv('GH_TOKEN')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.3"
    }
    if github_token:
        print("[+] Using GH_TOKEN for authenticated requests")
        headers["Authorization"] = f"Bearer {github_token}"
    else:
        print("[-] GH_TOKEN is not set, making unauthenticated requests")
    return headers

def make_request(host, url, headers):
    """Performs an HTTPS GET request and returns the response."""
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    if response.status != 200:
        raise GitHubRequestError(response.status, data, url)

    return data

def get_all_tags():
    """Fetches all tags from the GitHub repository, handling pagination."""
    tags = []
    page = 1

    while True:
        url = f"{GITHUB_API['tags']}?page={page}"
        headers = get_github_headers()
        
        try:
            data = make_request(GITHUB_API['base'], url, headers)
            results = json.loads(data)
        except Exception as e:
            raise Exception(f"[-] ERROR: request and parsing JSON failed on page {page}. {e}")

        if not results:
            break

        tags.extend([tag["name"] for tag in results])
        page += 1

    return tags

def get_all_dependencies(tags):
    """Extracts frida dependencies from setup.py or modern pyproject.toml metadata."""
    compatibility_matrix = {}

    for tag in tags:
        url = f"{GITHUB_RAW['tags']}/{tag}/setup.py"
        headers = get_github_headers()

        try:
            try:
                data = make_request(GITHUB_RAW['base'], url, headers)
            except GitHubRequestError as e:
                if e.status != 404:
                    raise
                url = f"{GITHUB_RAW['tags']}/{tag}/pyproject.toml"
                data = make_request(GITHUB_RAW['base'], url, headers)
                dependencies = tomllib.loads(data.decode()).get("project", {}).get("dependencies", [])
            else:
                dependencies = re.findall(r'''^\s*["'](frida\s*>=.*?)["'],?\s*$''', data.decode(), re.MULTILINE)

            for dependency in dependencies:
                match = re.fullmatch(r"frida\s*>=\s*([^,\s]+)\s*,\s*<\s*([^,\s]+)", dependency)
                if match:
                    compatibility_matrix[tag] = f">= {match[1]}, < {match[2]}"
                    break
            else:
                raise ValueError(f"frida version dependency not found in {url}")
        except Exception as e:
            raise Exception(f"[-] ERROR: dependency metadata read failed for tag {tag}. {e}") from e

    return compatibility_matrix

def get_structured_data(compatibility_matrix):
    """Return a structured dict from the compatibility matrix"""

    output = {}
    for frida_tools_version in compatibility_matrix:
        frida_version_str = compatibility_matrix[frida_tools_version]
        gte = frida_version_str.split(",")[0].split(">= ")[1].strip()
        lt = frida_version_str.split("< ")[1].strip()
        output[frida_tools_version] = {"gte": gte, "lt": lt}
    
    return output
