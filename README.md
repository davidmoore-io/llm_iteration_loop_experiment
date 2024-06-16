# OpenAI API CLI

This script allows you to interact with the OpenAI API (GPT-4) via a simple command-line interface.

## Prerequisites

- Python 3.12.2
- `venv` for virtual environment management

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd your_project
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**

    Ensure you have your OpenAI API key stored in an environment variable named `OPENAI_API_KEY`.

## Usage

### Basic Usage

To run the script with default settings:

```bash
python main.py "Your user input here"
```

### Specifying a System Prompt

You can specify a different system prompt file:

```bash
python main.py "Your user input here" --system_prompt ./path/to/your_system_prompt.txt
```

### Using a Configuration YAML File

You can use a configuration YAML file to specify the API key, base URL, and system prompt:

```bash
python main.py "Your user input here" --config ./config/example_config.yaml
```

Example `config/example_config.yaml`:

```yaml
api_key: "your_api_key_here"
api_base: "http://localhost:8000/v1"
system_prompt: "This is a custom system prompt."
```

### Multiple Runs

To run the model multiple times:

```bash
python main.py "Your user input here" --runs 5
```

The output will be saved in the `./output` directory with filenames indicating the date and run number.

## Additional Information

- The script will default to the public OpenAI API if no config file is specified.
- The script saves each run's output in a JSON file for easy inspection.

## Troubleshooting

If you encounter any issues, ensure that:
- Your Python version is 3.12.2.
- Your virtual environment is activated.
- All required libraries are installed.

For further assistance, please refer to the [OpenAI API documentation](https://github.com/openai/openai-python).