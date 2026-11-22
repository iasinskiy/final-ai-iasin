# Semester Week 12 Progress Report

## Completed Work

- Created mock JSON datasets for the customer support domain: `data/orders.json` (sample customer orders across `processing`, `shipped`, and `delivered` states), `data/faq.json` (store return, shipping, warranty, cancellation, and payment policies), and `data/tickets.json` (escalation storage).
- Implemented strict Pydantic v2 validation schemas in `src/schemas.py` covering tool input arguments (`OrderStatusInput`, `FAQSearchInput`, `SupportTicketInput`) and structured output records (`OrderRecord`, `FAQMatch`, `SupportTicketRecord`).
- Added custom regex field validation (`^ORD-\d{4,}$`) and normalization for `order_id` inputs, along with bounds checks and literal constraints for ticket priority levels.
- Verified schema integrity by parsing and validating all mock database records against `OrderRecord`.

## Important Commits

- Commit hash: *(will be updated after git push)*
- Description: Add mock JSON datasets (orders, FAQ, tickets) and Pydantic validation schemas for Week 12.

## Current Functionality

- Structured mock JSON data layer (`data/`) and strongly-typed Pydantic input/output models (`src/schemas.py`) ready to be bound to tool implementations.
- Working base `SupportAgent` prototype (`src/agent.py`) connected to OpenRouter (`gpt-5.6-luna`).

## Problems Encountered

- Ensuring consistent field naming and nullable handling (`tracking_number: Optional[str]`) between raw JSON records in `data/orders.json` and `OrderRecord` Pydantic models.

## Solutions

- Defined explicit `Optional[str] = None` defaults and `Literal` status enums in `src/schemas.py` and verified all entries via automated Python schema instantiation checks.

## What I Learned

- Designing Pydantic v2 custom `@field_validator` rules to sanitize and enforce strict format constraints on LLM-generated tool arguments before execution.
- Structuring local JSON mock stores to support deterministic tool responses and clean unit testing.

## Next Week

- Implement the three core Python tool functions (`get_order_status`, `search_faq`, `create_support_ticket`) in `src/tools.py` backed by the JSON datasets and Pydantic schemas.
- Define OpenAI-compatible JSON Schema tool specifications for LLM function calling.