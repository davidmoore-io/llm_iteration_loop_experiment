# Developer Notes

This project was entirely generated by ChatGPT (4o), including the blogpost included in the project, and the README blow.

I've not touched the code at all, nor have I edited any of its outputs manually. The only human writing here is in this notes section... despite the near overwhelming urge to intervene at various points along the way as I watched it make mistakes. I was determined to do nothing other than ask it to do things for me.

It's an experiment in using ChatGPT 4o plus prompt engineering techniques to create a complete python project, applying prompt engineering and iteration techniques to get it to fix its own errors.

I also got it to read my past blog posts (all of which were entirely written by me, manually, like a big ol' Scottish, slightly hungover monkey with a keyboard) to mimic the style of my writing.

To keep the whole experiment peak meta, I asked ChatGPT 4o to create a python project that allows me to experiment with auto-generation of Python projects using automated, iterative calls to the OpenAI API, feeding back its own outputs alongside instructions (a 'system prompt') to improve the quality of its code and approach. It did this successfully on its own, albeit I steered it along the way.

I spent a Sunday afternoon on this (3 and bit hours). I could've (probably) created the project and written the post myself in the same timeframe (ish), particularly if I'd used GitHub CoPilot to generate some of the code.

However... and it's a big 'however'... bear in mind that I'm not a proper developer anymore and haven't been for about 10 years.

This demonstrates in the hands of someone that at least half knows what they're doing, almost anyone can get pretty solid outputs out of the public versions of these tools.

Based on another (currently stealth-mode) project that I'm involved in, I know that AI agents combined with more complex prompt engineering techniques deal with some of the issues I came up against, but it still blows my mind that a single AI model using a simple chat interface that my gran could use can do what this experiment got it to do.

It got into a mess at the end when I asked it to update the blog post, presumably because the system prompts and various other self-referential 'stuff' was in there, but as I said... it's so, so close to scary brilliance. We're inches away from AI tools fully automating very human-shaped problems, and that's going to have complex impacts on how we all operate and work day to day.

The transcript of my interactions with ChatGPT is available [here](https://chatgpt.com/share/0a5c986f-5267-4e1f-9760-fd28f17438ef).
The git repository, including all the code, prompts, this blog post, and the full commit history as I iterated through the project, is available [here](https://github.com/davidmoore-io/llm_iteration_loop_experiment).

Everything in the README below, all the code, and the blog post (excluding the notes section at the top) was entirely written by ChatGPT 4o.

If you've never attempted or seen anything like this before, everything from here on should be pretty mind-blowing and probably a smidge scary. It still freaks me out a bit, and I've been using these things for a long time now...

Enjoy. Meet ChatGPT, doing its best `Dave - Blog Writer` and `David - Python Developer` impression...

---

# OpenAI API CLI

## Introduction

AI tools like GPT-4o have transformed how we approach software development. Recently, I collaborated with ChatGPT to create a Python script that interacts with the OpenAI API. This iterative process, emphasising careful code review and continuous improvement, underscores the potential of AI in streamlining project development. The project was intended as a quick experiment in iteration and feedback loops in large language models, with a view to integrating the approach into an AI agent project down the line.

## Project Purpose

The primary objective of this project is to experiment with GPT-4o and iterative loops to enhance the output of AI agent-based systems. By leveraging iterative prompts and feedback cycles, we aim to refine the responses generated by the AI, ultimately achieving more accurate and useful outputs.

## Prerequisites

- Python 3.12.2
- `venv` for virtual environment management

## Setup

### Mac and Linux

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

### Windows

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd your_project
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
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
python main.py
```

### Specifying a System Prompt

You can specify a different system prompt file:

```bash
python main.py --system_prompt ./path/to/your_system_prompt.txt
```

### Using a Configuration YAML File

You can use a configuration YAML file to specify the API key, base URL, and system prompt:

```bash
python main.py --config ./config/example_config.yaml
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
python main.py --runs 5
```

The output will be saved in the `./output` directory with filenames indicating the date and run number.

## Project Structure and Configuration

The project consists of several files:

- `main.py`: The primary script.
- `requirements.txt`: Lists necessary libraries.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Provides setup and usage instructions.
- Default system prompt and configuration YAML files.
- User input prompt file.

## Lessons Learned and Best Practices

Throughout the process, several best practices emerged:

- **Take a Breath, Think Step by Step**: This mantra ensures a methodical approach, minimising errors and improving efficiency.
- **Code Review and Testing**: Iterative code review is essential for maintaining high code quality.
- **Prompt Experimentation**: Experimenting with different prompts and iterative cycles helps refine outputs.

## Additional Information

- The script will default to the public OpenAI API if no config file is specified.
- The script saves each run's output in a JSON file for easy inspection.

## Troubleshooting

If you encounter any issues, ensure that:

- Your Python version is 3.12.2.
- Your virtual environment is activated.
- All required libraries are installed.

For further assistance, please refer to the [OpenAI API documentation](https://github.com/openai/openai-python).

## Conclusion

This project demonstrates the potential of using GPT-4o to create functional, complete projects quickly. The iterative approach, combined with prompt experimentation and careful code review, ensures high-quality and efficient outputs. As AI continues to evolve, such methodologies will become increasingly valuable in various domains, enabling rapid development and innovation.

For more detailed insights and the complete project, visit the [GitHub repository](https://github.com/your-repo-link).
```

This `README.md` now includes the developer notes, setup instructions for Mac, Linux, and Windows, and all other necessary information to run the project. Let me know if you need any further adjustments!