# parser.py

import json


def parse_sarif(sarif_file_path):
    """
    Parses a SARIF file to extract vulnerability details.

    Parameters:
    - sarif_file_path: Path to the SARIF file.

    Returns:
    - A list of dictionaries, each containing details about a vulnerability.
    """
    vulnerabilities = []

    try:
        with open(sarif_file_path, 'r', encoding='utf-8') as file:
            sarif_data = json.load(file)

        # Extract runs from the SARIF data
        for run in sarif_data.get('runs', []):
            # Extract results (vulnerabilities) from each run
            for result in run.get('results', []):
                vulnerability = {
                    'rule_id': result.get('ruleId'),
                    'message': result.get('message', {}).get('text'),
                    'severity': result.get('level'),
                    'file': result.get('locations', [])[0].get('physicalLocation', {}).get('artifactLocation', {}).get('uri'),
                    'snippet': result.get('locations', [])[0].get('physicalLocation', {}).get('region', {}).get('snippet', {}).get('text'),
                    'description': result.get('rule', {}).get('fullDescription', {}).get('text'),
                    'region': result.get('locations', [])[0].get('physicalLocation', {}).get('region', {})
                }
                vulnerabilities.append(vulnerability)

    except Exception as e:
        print(f"Error parsing SARIF file: {e}")
        vulnerabilities = []  # Reset vulnerabilities list in case of error

    return vulnerabilities
