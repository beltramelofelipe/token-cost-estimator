# CLAUDE.md — AI Assistant Guide for token-cost-estimator

## Project Overview

A minimal Python script that combines **Docling** (IBM) and **Tiktoken** (OpenAI) to:
1. Convert documents (PDFs via URL or local file) to Markdown
2. Count LLM tokens using official OpenAI tokenization
3. Estimate the input cost for processing that document through a GPT model

**Language:** Python 3.10+
**Primary file:** `token-cost.py`

---

## Repository Structure

```
token-cost-estimator/
├── token-cost.py   # Main script: document conversion + cost estimation
└── README.md       # Project documentation (written in Portuguese)
```

No package manager config, no test suite, no CI/CD — this is a single-purpose utility script.

---

## Core Logic

### `estimate_cost(text, model_name="gpt-4o")` — `token-cost.py:5`

Takes a string and a model name, returns `(total_tokens, cost)`.

**Supported models and prices ($/1M input tokens):**
| Model | Price |
|---|---|
| `gpt-4o` | $2.50 |
| `gpt-4o-mini` | $0.15 |
| `gpt-3.5-turbo` | $0.50 |

**Cost formula:**
```
cost = (total_tokens / 1_000_000) * price_per_million
```

Unknown model names return cost of `$0.00` (via `.get(model_name, 0)`).

### Execution block — `token-cost.py:21`

Hardcoded to:
1. Fetch the ArXiv paper `https://arxiv.org/pdf/2408.09869`
2. Convert it to Markdown via `DocumentConverter`
3. Run `estimate_cost` with `gpt-4o`
4. Print a Portuguese-language report

---

## Dependencies

Install manually — no `requirements.txt` exists:

```bash
pip install docling tiktoken
```

| Package | Purpose |
|---|---|
| `docling` | PDF/document → Markdown conversion (IBM) |
| `tiktoken` | Tokenization matching OpenAI API behavior |

---

## Development Conventions

- **Language:** Python, snake_case naming, PEP 8 style
- **No docstrings or inline comments** currently in the codebase — add them if introducing new functions
- **No error handling** — the script will raise exceptions on network failures, unsupported models, or malformed documents
- **Pricing is hardcoded** in the `pricing` dict inside `estimate_cost`; update it there when OpenAI changes prices
- **Output language:** Portuguese (`Relatório de Processamento`, `Tokens detectados`, `Custo estimado`)
- **No environment variables** — no API keys required (Docling fetches PDFs directly, tiktoken works offline)

---

## Running the Script

```bash
python token-cost.py
```

Expected output:
```
📊 Relatório de Processamento:
--- Tokens detectados: <N>
--- Custo estimado (Input): $<price>
```

Note: First run downloads the Docling model weights — this may take several minutes.

---

## Known Limitations / Things to Be Aware Of

- The source URL (`https://arxiv.org/pdf/2408.09869`) is hardcoded; changing the target document requires editing the script directly
- No output token cost estimation (only input tokens)
- `tiktoken` is OpenAI-specific; it does not tokenize correctly for Anthropic, Google, or other providers
- No test suite exists — validate behavior manually by comparing token counts against the OpenAI Tokenizer playground
- `pricing.get(model_name, 0)` silently returns $0 for unknown models rather than raising an error

---

## Git Workflow

- **Main branch:** `main`
- **Feature branches:** use descriptive names, e.g. `claude/add-claude-documentation-WovLe`
- **Commit style:** short imperative messages (e.g. `add token-cost`, `add projeto`)
- No pre-commit hooks or linting configured

---

## What Does NOT Exist (Do Not Assume)

- No `requirements.txt` or `pyproject.toml`
- No test files or test framework
- No CI/CD pipelines
- No `.env` or environment variable configuration
- No modular package structure — everything is in a single script
- No output cost estimation (only input)
