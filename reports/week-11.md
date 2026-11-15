# Semester Week 11 Progress Report

## Completed Work

- Created and activated Python 3.14 virtual environment (`.venv`) and defined project dependencies (`openai`, `pydantic`, `python-dotenv`, `pytest`) in `requirements.txt`.
- Configured secure environment variable management using `.env` and added `.env.example` template while ensuring `.env` and `.venv/` are excluded in `.gitignore`.
- Integrated OpenRouter API via the OpenAI-compatible Python SDK and implemented the initial `SupportAgent` prototype in `src/agent.py` running `gpt-5.6-luna`.
- Verified end-to-end API connectivity and system prompt adherence with a sample customer order inquiry (`ORD-1001`).
- Updated `reports/proposal.md` model selection section to match the configured OpenRouter endpoint and model.

## Important Commits

- Commit hash: *(will be updated after git push)*
- Description: Set up Python environment, OpenRouter integration, initial SupportAgent prototype, and Week 11 report.

## Current Functionality

- Working CLI prototype (`src/agent.py`) capable of initializing `SupportAgent`, loading API credentials from `.env`, and generating grounded conversational responses via `gpt-5.6-luna`.

## Problems Encountered

- Default `python` command triggered the Windows Store alias instead of the installed Python 3.14 interpreter.
- PowerShell execution policy blocked activation of `.venv\Scripts\Activate.ps1`.
- Initial script configuration looked for `OPENAI_API_KEY` instead of `OPENROUTER_API_KEY`.

## Solutions

- Created the virtual environment explicitly using `py -m venv .venv`.
- Enabled script execution for the current terminal session via `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
- Configured `OpenAI` client in `src/agent.py` with `base_url="https://openrouter.ai/api/v1"` and loaded `OPENROUTER_API_KEY` and `MODEL_NAME` via `python-dotenv`.

## What I Learned

- Configuring OpenAI-compatible SDK clients for third-party API providers like OpenRouter.
- Structuring Python agent projects with isolated virtual environments and secure environment variable templates.

## Next Week

- Create mock JSON datasets for customer orders (`data/orders.json`) and store FAQs (`data/faq.json`).
- Define Pydantic models for strict input/output validation of tool arguments and responses.\

## Important Commits

- Commit hash: `57d17e3`
- Description: Set up Python environment, OpenRouter integration, initial SupportAgent prototype, and Week 11 report.