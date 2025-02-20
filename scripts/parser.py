import os
import json
import http.client

GITHUB_API = {
    'base': "api.github.com",
    'tags': "/repos/frida/frida-tools/tags"
}
GITHUB_RAW = {
    'base': "raw.githubusercontent.com",
    'tags': "/frida/frida-tools/refs/tags"
}

FRIDA_TOOLS_REPO = "frida/frida-tools"

def get_github_headers():
    """Returns GitHub authentication headers if a token is available."""
    github_token = os.getenv('LOCAL_GITHUB_TOKEN')
    headers = {
        "User-Agent": "Python-http.client"
    }
    if github_token:
        headers["Authorization"] = f"token {github_token}"
    return headers

def make_request(host, url, headers):
    """Performs an HTTPS GET request and returns the response."""
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", url, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    if response.status != 200:
        raise Exception(f"[-] ERROR: status code {response.status} - error {data.decode()} - url {url}")

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
    """Retrieves setup.py content for each tag and extracts frida version dependencies."""
    compatibility_matrix = {}

    for tag in tags:
        url = f"{GITHUB_RAW['tags']}/{tag}/setup.py"
        headers = get_github_headers()

        try:
            data = make_request(GITHUB_RAW['base'], url, headers)
        except Exception as e:
            raise Exception(f"[-] ERROR: raw content read failed for tag {tag}. {e}")

        setup_content = data.decode()
        for line in setup_content.splitlines():
            stripped_line = line.strip()
            if stripped_line.startswith('"frida >='):
                compatible_versions = stripped_line.replace('"frida ', '').replace('",', '')
                compatibility_matrix[tag] = compatible_versions
                break

    return compatibility_matrix