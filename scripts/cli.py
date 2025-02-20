from parser import get_all_tags, get_all_dependencies

# Don't look at this code, it is very ugly
# but I wanted to print a table without using external deps

def print_as_table(compatibility_matrix):
    frida_tools_str = "frida-tools"
    frida_str = "frida"
    longest_value = max(compatibility_matrix.values(), key=len)
    spaces = (len(longest_value)-len(frida_str))*' '
    frida_str = f"{frida_str}{spaces}"
    print()
    print(f"| {frida_tools_str} | {frida_str} |")
    print(f"|-{len(frida_tools_str)*'-'}-+-{len(frida_str)*'-'}-|")

    for frida_tool_version in compatibility_matrix:
        frida_version = compatibility_matrix[frida_tool_version]
        spaces_after_1 = (len(frida_tools_str)-len(frida_tool_version))*' '
        spaces_after_2 = (len(frida_str)-len(frida_version))*' '
        print(f"| {frida_tool_version}{spaces_after_1} | {frida_version}{spaces_after_2} |")

if __name__ == "__main__":
    print("[+] Getting all tags...")
    tags = get_all_tags()
    print(f"[+] Tags correctly retrieved, there are {len(tags)} tags available")
    print("[+] Getting all dependency versions to build compatibility matrix")
    compatibility_matrix = get_all_dependencies(tags)
    print_as_table(compatibility_matrix)