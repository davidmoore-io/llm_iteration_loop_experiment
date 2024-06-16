from openai import OpenAI
import argparse
import yaml
import os
import json
from datetime import datetime
import tiktoken  # Ensure you have the tiktoken library installed

def load_system_prompt(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise FileNotFoundError(f"Could not read the system prompt file: {e}")

def load_user_input(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise FileNotFoundError(f"Could not read the user input prompt file: {e}")

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise FileNotFoundError(f"Could not read the config file: {e}")

def save_output(output, run_number, output_dir='./output'):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = datetime.now().strftime("%d-%Y")
        filename = f"{output_dir}/{timestamp}-run-{run_number}.json"
        with open(filename, 'w') as file:
            json.dump(output, file, indent=4)
        print(f"Output saved to {filename}")
    except Exception as e:
        raise IOError(f"Could not save the output: {e}")

def call_openai_api(system_prompt, user_input, api_key, api_base=None):
    max_tokens = 4096
    encoding = tiktoken.encoding_for_model("gpt-4")

    system_tokens = encoding.encode(system_prompt)
    user_tokens = encoding.encode(user_input)
    total_tokens = len(system_tokens) + len(user_tokens)

    while total_tokens > max_tokens:
        if len(system_tokens) > len(user_tokens):
            system_tokens = system_tokens[:len(system_tokens) - (total_tokens - max_tokens)]
        else:
            user_tokens = user_tokens[:len(user_tokens) - (total_tokens - max_tokens)]
        total_tokens = len(system_tokens) + len(user_tokens)

    truncated_system_prompt = encoding.decode(system_tokens)
    truncated_user_input = encoding.decode(user_tokens)

    try:
        print("Initializing OpenAI client")
        client = OpenAI(api_key=api_key)
        if api_base:
            client.api_base = api_base

        api_call_params = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": truncated_system_prompt},
                {"role": "user", "content": truncated_user_input}
            ],
            "max_tokens": max_tokens - total_tokens  # Subtracting input tokens from max_tokens
        }

        print("\nMaking API call to OpenAI with the following parameters:")
        print(json.dumps(api_call_params, indent=4))

        response = client.chat.completions.create(**api_call_params)

        print("\nAPI call successful. Response:")
        response_dict = response.to_dict()
        print(json.dumps(response_dict, indent=4))

        return response_dict['choices'][0]['message']['content']
    except Exception as e:
        print("\nAPI call failed with the following parameters:")
        print(json.dumps(api_call_params, indent=4))
        raise RuntimeError(f"API call failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="OpenAI API CLI")
    parser.add_argument('--system_prompt', type=str, default='./input/default_system_prompt.txt', help="Path to the system prompt file")
    parser.add_argument('--user_input_prompt', type=str, default='./input/user_input_prompt.txt', help="Path to the user input prompt file")
    parser.add_argument('--config', type=str, help="Path to the configuration YAML file")
    parser.add_argument('--runs', type=int, default=1, help="Number of times to run the model")
    args = parser.parse_args()

    try:
        if args.config:
            print("Loading configuration from file")
            config = load_config(args.config)
            api_key = config.get('api_key')
            api_base = config.get('api_base')
            system_prompt = config.get('system_prompt', load_system_prompt(args.system_prompt))
        else:
            print("Loading configuration from environment variables")
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
            api_base = None
            system_prompt = load_system_prompt(args.system_prompt)

        user_input = load_user_input(args.user_input_prompt)

        for run_number in range(1, args.runs + 1):
            print(f"\nRun number: {run_number}")
            output = call_openai_api(system_prompt, user_input, api_key, api_base)
            save_output(output, run_number)

            # Prepare for the next run if needed
            user_input = output

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
