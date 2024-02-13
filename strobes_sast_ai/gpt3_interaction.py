# gpt3_interaction.py

from openai import OpenAI
from .config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)


def query_gpt3_for_patch(vulnerability):
    """
    Constructs a prompt for GPT-3 based on the vulnerability information.

    Parameters:
    - vulnerability: A dictionary containing details of the vulnerability.

    Returns:
    - A string representing the prompt for GPT-3.
    """
    # Example prompt construction, customize based on your SARIF parsing and requirements
    intructions = """
    Your role involves identifying and fixing security vulnerabilities in user-submitted code snippets. Responses must strictly adhere to a JSON format. Each response should include a "patch" key with the corrected code, an "imports_required" key indicating whether new imports are necessary (true/false), and an "imports" key listing any additional imports needed at the start of the file. Refrain from providing explanations, commentary, or descriptions. Your response should focus solely on presenting the secure code solution, specifying any new imports required at the beginning. Example response format: {"patch": "json.load(open('./models/cwe_cls.json'))", "imports_required": "true", "imports": "import json"}.
    """
    prompt = f"Given the following code vulnerability: {str(vulnerability)}, return a patch."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "system", "content": intructions}, {
            "role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(completion.choices[0].message.content)
