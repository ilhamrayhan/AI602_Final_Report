# LLM Debate Project

This project reproduces and extends the debate-based truthfulness evaluation of Khan et al. (2024). It implements a structured debate pipeline using large language models (LLMs) to assess truthfulness through adversarial argumentation and judging. Due to financial constraints and the lack of free trial credits, this project uses mocked outputs to simulate LLM responses and judge decisions. Nonetheless, the pipeline is fully implemented and ready to be executed with real API calls when an appropriate API budget is available.

## Project Structure

- `data/` — Input questions (TruthfulQA) and related datasets.
- `results/` — Experiment outputs, including logs, results, and illustrative graphs.
- `experiments/` — Python scripts for running consultancy and debate experiments, including the implementation of proposed improvements (verbosity control, tool-free evaluation, and speaker randomization).

## Environment Setup

This project uses the [Mamba](https://mamba.readthedocs.io/) package manager for environment management.

To set up the environment, run:
```bash
mamba env create -f environment.yml
mamba activate llm-debate
```


## API Usage and Mocked Outputs
The experiment scripts are designed to run with OpenAI's GPT-4 and GPT-3.5 models through the OpenAI API.

Due to financial constraints, this project uses mocked outputs to simulate LLM responses and judge decisions. The code structure supports easy switching between mocked and real API calls.

**Note:** Before running with real API calls, you must set your OpenAI API key in a `.env` file:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Ensure that you have sufficient API credits or billing set up on your OpenAI account.

## How to Run

1. Edit the `experiments/generate_questions.py` script if you wish to customize the question set.
2. Run the pipeline:
```bash
python experiments/debate_experiment.py
```

3. Review logs and outputs in the `results/` folder.

## Future Work

- Integrate real API calls once API credits are available.
- Extend the pipeline to incorporate human judges and multimodal evaluation.
- Empirically test improvements (verbosity control, tool-free evaluation, and speaker randomization) on real LLM outputs.

## Acknowledgments

This project was developed as part of a course assignment AI602 Advanced Deep Learning at KAIST. Special thanks to Khan et al. (2024) for their foundational work on debate protocols in LLMs.


