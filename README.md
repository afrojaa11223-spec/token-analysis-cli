# Token Analysis CLI

A Python command-line tool for analyzing text tokenization using OpenAI's `tiktoken` library.

## Features

- Character and UTF-8 byte counting.
- Token ID and token count analysis.
- Bytes-per-token calculation.
- English and Bangla tokenization comparison.
- Unicode normalization (NFKC).
- Before-and-after normalization comparison.
- Estimated API input cost calculation.
- Visual representation of token splits.

## Technologies

- Python 3
- tiktoken
- argparse
- unicodedata
- re

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd token-analysis-cli
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependency:

```bash
pip install tiktoken
```

## Usage

Analyze an English text file:

```bash
python3 token_report.py english.txt
```

Analyze a Bangla text file:

```bash
python3 token_report.py bangla.txt
```

Visualize token splits:

```bash
python3 token_report.py bangla.txt --viz
```

Select a tokenizer encoding:

```bash
python3 token_report.py english.txt --encoding cl100k_base
```

## Sample Results

| Measurement | English | Bangla |
|---|---:|---:|
| Characters | 96 | 87 |
| UTF-8 Bytes | 96 | 237 |
| Tokens | 17 | 108 |
| Bytes per Token | 5.65 | 2.19 |

## Key Learning

Bangla text can require significantly more tokens than English text. This happens because tokenization depends on the tokenizer's learned vocabulary and subword patterns. UTF-8 byte length also differs between the two writing systems.

## API Cost

The project uses an illustrative input-token price of $2 per million tokens.

Actual API pricing depends on the selected provider and model.

## Author

Created as part of an AI Security training assignment.
