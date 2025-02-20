import os
import re
from parser import get_all_tags, get_all_dependencies

def update_readme(compatibility_matrix):
    # Get the absolute path of the script's directory (scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the README.md file in the root directory
    readme_path = os.path.join(script_dir, "..", "README.md")

    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    frida_tools_str = "`frida-tools`"
    frida_str = "`frida`"
    longest_value = max(compatibility_matrix.values(), key=len)
    spaces = (len(longest_value)-len(frida_str))*' '
    frida_str = f"{frida_str}{spaces}"

    # Define the Markdown table headers
    table_header = f"| {frida_tools_str} | {frida_str} |\n| {len(frida_tools_str)*'-'} | {len(frida_str)*'-'} |\n"
    
    # Convert dictionary data into Markdown table rows
    table_rows = "\n".join(f"| {key}{(len(frida_tools_str)-len(key))*' '} | {value}{(len(frida_str)-len(value))*' '} |" 
                           for key, value in compatibility_matrix.items())
    table_content = table_header + table_rows + "\n"

    # Regex pattern to capture everything between "## Compatibility Matrix" and the next "##" heading (## Bar or another heading)
    pattern = re.compile(r"(## Compatibility Matrix\n)(.*?)(?=\n## )", re.DOTALL)

    # Replace the old content with "## Compatibility Matrix" followed by the new table
    updated_content = re.sub(pattern, r"\1\n" + table_content, content)

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    print("[+] Getting all tags...")
    tags = get_all_tags()
    print(f"[+] Tags correctly retrieved, there are {len(tags)} tags available")
    print("[+] Getting all dependency versions to build compatibility matrix")
    compatibility_matrix = get_all_dependencies(tags)
    print("[+] Dependency versions correctly retrieved, updating compatibility matrix table...")
    update_readme(compatibility_matrix)
    print("[+] README.md file correctly updated")

