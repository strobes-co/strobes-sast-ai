# patcher.py

import os


def apply_patch(patch_data, vulnerability_data):
    file_path = vulnerability_data.get('file')
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return False

    # Extract relevant data from the vulnerability and patch information
    snippet_to_replace = vulnerability_data['region']['snippet']['text']
    patch_content = patch_data['patch']
    imports_required = patch_data['imports_required']
    imports_content = patch_data.get('imports', '')

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check and add imports if required
        if imports_required:
            if imports_content + '\n' not in lines[0]:
                # Ensure imports are added correctly
                lines.insert(0, imports_content + '\n\n')

        # Replace the snippet in the target line(s)
        replaced = False
        for i, line in enumerate(lines):
            if snippet_to_replace in line:
                lines[i] = line.replace(snippet_to_replace, patch_content)
                replaced = True
                break  # Remove this break if you want to replace all occurrences

        if not replaced:
            print(
                f"Warning: The snippet to replace was not found in {file_path}.")
            return False

        # Write the changes back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Patch applied successfully to {file_path}.")
        return True
    except Exception as e:
        print(f"Error applying patch to {file_path}: {e}")
        return False
