# cli.py

from strobes_sast_ai.gpt3_interaction import query_gpt3_for_patch
from strobes_sast_ai.parser import parse_sarif
from strobes_sast_ai.patcher import apply_patch
from strobes_sast_ai.ai_patch_suggester import decide_on_patch


def process_sarif_file(file_path, dry_run=False):
    vulnerabilities = parse_sarif(file_path)
    print(f"Found {len(vulnerabilities)} vulnerabilities to process.")

    patched_files = []
    verification_needed = []
    imports_added = []

    for vulnerability in vulnerabilities:
        patch_data = query_gpt3_for_patch(vulnerability)
        patch_decision = decide_on_patch(vulnerability, patch_data)
        if patch_decision and not dry_run:
            success = apply_patch(patch_data, vulnerability)
            if success:
                patched_files.append(vulnerability['file'])
                if patch_data.get('imports_required'):
                    imports_added.append(vulnerability['file'])
            else:
                verification_needed.append(vulnerability['file'])
        elif dry_run:
            print(f"Would patch {vulnerability['file']}: {patch_data}")

    return patched_files, verification_needed, imports_added


def print_summary_table(patched_files, verification_needed, imports_added):
    print("\nSummary:")
    print(f"{'File':<50} | {'Status':<20} | {'Imports Added':<15}")
    print("-" * 90)
    for file in patched_files:
        imports_status = "Yes" if file in imports_added else "No"
        print(f"{file:<50} | {'Patched':<20} | {imports_status:<15}")
    for file in verification_needed:
        print(f"{file:<50} | {'Verification Needed':<20} | {'N/A':<15}")


def main(sarif_file, dry_run=False):
    """
    Strobes-SAST-AI: A tool for automatically patching security vulnerabilities identified by SAST tools using OpenAI's GPT-3.
    """

    patched_files, verification_needed, imports_added = process_sarif_file(
        sarif_file, dry_run)
    print_summary_table(patched_files, verification_needed, imports_added)


if __name__ == '__main__':
    main()
