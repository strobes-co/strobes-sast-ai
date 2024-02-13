# Strobes-SAST-AI

`strobes-sast-ai` is an innovative command-line interface (CLI) tool designed to automate the patching of security vulnerabilities identified by Static Application Security Testing (SAST) tools. Utilizing the power of OpenAI's GPT-3, `strobes-sast-ai` intelligently suggests and applies patches to vulnerabilities reported in the SARIF (Static Analysis Results Interchange Format) output, streamlining the remediation process and enhancing software security posture.

## Features

- Automated parsing of SARIF files to identify security vulnerabilities.
- Integration with OpenAI's GPT-3 for generating intelligent patch suggestions.
- Automated application of patches to vulnerable files.
- CLI support for easy integration into existing workflows and CI/CD pipelines.

## Prerequisites

Before installing `strobes-sast-ai`, ensure you have the following:

- Python 3.6 or newer
- pip (Python package installer)
- An active OpenAI API key for accessing GPT-3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourrepository/strobes-sast-ai.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd strobes-sast-ai
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

To use `strobes-sast-ai`, you must configure it with your OpenAI API key. This key enables the tool to communicate with the GPT-3 API for generating patch suggestions.

1. Locate the `config.py` file in the `strobes_sast_ai` directory.
2. Open `config.py` in a text editor and replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key:
   ```python
   OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
   ```

## Usage

To run `strobes-sast-ai`, use the following command from the root directory of the project:

```bash
python -m strobes_sast_ai.cli --sarif-file /path/to/your/sarif/file.sarif
```

### Options

- `--sarif-file`: Specifies the path to the SARIF file containing the SAST findings.
- `--dry-run`: Simulates the patching process without making any changes to the files, useful for testing.

## Contributing

We welcome contributions to `strobes-sast-ai`! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

## License

`strobes-sast-ai` is released under the MIT License. See the LICENSE file for more details.

## Disclaimer

`strobes-sast-ai` is a tool intended to assist in the security patching process. While it aims to automate patch suggestions and applications, always review and test patches thoroughly before applying them in a production environment.

