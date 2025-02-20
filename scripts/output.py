import os
import json
from parser import get_all_tags, get_all_dependencies, get_structured_data

if __name__ == "__main__":
    # Get the absolute path of the script's directory (scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to the README.md file in the root directory
    output_filepath = os.path.join(script_dir, "..", "frida-compatibility-matrix.json")

    print("[+] Getting all tags...")
    tags = get_all_tags()
    print(f"[+] Tags correctly retrieved, there are {len(tags)} tags available")
    print("[+] Getting all dependency versions to build compatibility matrix")
    compatibility_matrix = get_all_dependencies(tags)
    output_data = get_structured_data(compatibility_matrix)
    print("[+] Saving output file...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)