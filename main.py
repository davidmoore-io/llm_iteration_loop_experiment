import openai
from openai import OpenAI
import argparse
import yaml
import os
import json
from datetime import datetime

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
    except Exception as e:
        raise IOError(f"Could not save the output: {e}")

def call_openai_api(system_prompt, user_input, api_key, api_base=None):
    try:
        openai.api_key = api_key
        if api_base:
            openai.api_base = api_base

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
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
            config = load_config(args.config)
            api_key = config.get('api_key')
            api_base = config.get('api_base')
            system_prompt = config.get('system_prompt', load_system_prompt(args.system_prompt))
        else:
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
            api_base = None
            system_prompt = load_system_prompt(args.system_prompt)

        user_input = load_user_input(args.user_input_prompt)

        for run_number in range(1, args.runs + 1):
            output = call_openai_api(system_prompt, user_input, api_key, api_base)
            save_output(output, run_number)

            # Prepare for the next run if needed
            user_input = output

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
