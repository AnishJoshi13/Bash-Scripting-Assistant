# Bash Scripting Coding Assistant

## Overview

This repository contains a basic chat interface that helps users convert natural language input into bash scripts. A fine-tuned version of the CodeLlama-7b model trained on a custom dataset is used. The dataset is of natural language commands and their corresponding Bash script outputs, making it capable of generating Bash scripts from natural language input prompts. The dataset is available on Hugging Face as [AnishJoshi/nl2bash-custom](https://huggingface.co/datasets/AnishJoshi/nl2bash-custom)
The finetuned model is also public on HuggingFace as [AnishJoshi/codellama2-finetuned-nl2bash-fin](https://huggingface.co/AnishJoshi/codellama2-finetuned-nl2bash-fin)


## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [Acknowledgments](#acknowledgments)
6. [Contact](#contact)
7. [TODO](#todo)

## Installation
### Prerequisites
- Bash Shell [Ubuntu WSL](https://ubuntu.com/desktop/wsl)
- [Python 3.10 (preferred 3.10.10)](https://www.python.org/downloads/release/python-31010/)
- [Jupyter Notebook](https://jupyter.org/install)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AnishJoshi13/Bash-Scripting-Assistant
   ```
2. Navigate to the project directory:
   ```bash
   cd Bash-Scripting-Assistant/
   ```
3. Run the installation script:
   ```bash
   ./install.sh
   ```

## Usage
To start using the assistant, run:
```bash
streamlit run app/chat_interface.py
```


## Features
- **Auto-completion**: Provides context-aware suggestions to complete your commands.
- **Error-checking**: Identifies common errors in your Bash scripts.
- **Code Explanation**: Explains the generated bash code line by line.


## Contributing
All contributions are welcome! Please check [TODO](#todo) for future plans

## Acknowledgments
Thanks to these research papers for helping me curate the dataset

- @inproceedings{LinWZE2018:NL2Bash, author = {Xi Victoria Lin and Chenglong Wang and Luke Zettlemoyer and Michael D. Ernst}, title = {NL2Bash: A Corpus and Semantic Parser for Natural Language Interface to the Linux Operating System}, booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation {LREC} 2018, Miyazaki (Japan), 7-12 May, 2018.}, year = {2018} }

- @article{Fu2021ATransform, title={A Transformer-based Approach for Translating Natural Language to Bash Commands}, author={Quchen Fu and Zhongwei Teng and Jules White and Douglas C. Schmidt}, journal={2021 20th IEEE International Conference on Machine Learning and Applications (ICMLA)}, year={2021}, pages={1241-1244} }

- @article{fu2023nl2cmd, title={NL2CMD: An Updated Workflow for Natural Language to Bash Commands Translation}, author={Fu, Quchen and Teng, Zhongwei and Georgaklis, Marco and White, Jules and Schmidt, Douglas C}, journal={Journal of Machine Learning Theory, Applications and Practice}, pages={45--82}, year={2023} }

## Contact
For support, feedback and project collaborations please contact [Anish Joshi](mailto:anish.yog10@gmail.com) or [Anish Joshi - LinkedIn](https://www.linkedin.com/in/anish-joshi-58a265229/)

## TODO

A lot of feature addtions can be done so that the assistant is workspace compatible to be used commercially

- Improve UI
- Handle conversation history
- Contextual response generation
- Code verification loop and error correction

