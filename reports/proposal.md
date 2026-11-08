# Project Proposal — Semester Week 10

## Project Title

Smart Customer Support & Escalation Agent

## Problem Description

E-commerce and service platforms face high volumes of repetitive customer inquiries regarding order tracking, return policies, and general store FAQs. Processing these requests manually increases operational costs and causes response delays. 

This project implements an intelligent LLM-powered customer support agent capable of dynamically executing system actions via tools, querying a structured knowledge base, validating customer input arguments, and escalating complex or unresolved issues to human support.

## Target Users

- E-commerce customers seeking instant automated assistance regarding orders and store policies.
- Support operations teams requiring automated triage and handling of routine customer inquiries.

## Selected Difficulty

C — Intermediate

## Expected Functionality

- Natural language query understanding and intent classification.
- Dynamic LLM-driven tool selection and parameter extraction.
- Real-time order status tracking via structured database lookups.
- Grounded store policy retrieval using a local FAQ/Knowledge Base.
- Automated support ticket generation and human escalation for unresolved or complex requests.
- Strict argument validation and error handling for failed tool calls.

## Proposed Functions

### 1. `get_order_status`
- **Name:** `get_order_status`
- **Purpose:** Retrieves real-time status and shipping details for a specific order.
- **Inputs:** `order_id` (str) — The unique identifier for the customer's order (e.g., `"ORD-1001"`).
- **Outputs:** `dict` containing order state, tracking number, items, and estimated delivery date.
- **Dependencies:** Local JSON database / Mock Order Management System.

### 2. `search_faq`
- **Name:** `search_faq`
- **Purpose:** Queries the internal knowledge base to find relevant store policies and procedural answers.
- **Inputs:** `query` (str) — Search keywords or customer intent string (e.g., `"return policy"`).
- **Outputs:** `list[dict]` containing matching policy questions, answers, and relevance scores.
- **Dependencies:** Local JSON knowledge base / vector index.

### 3. `create_support_ticket`
- **Name:** `create_support_ticket`
- **Purpose:** Escalates complex or high-priority customer issues to human operators by generating a ticket.
- **Inputs:** 
  - `user_id` (str) — Identifier of the customer.
  - `issue_description` (str) — Summary of the problem.
  - `priority` (str) — Ticket urgency level (`"low"`, `"medium"`, `"high"`).
- **Outputs:** `dict` containing ticket ID, creation timestamp, and confirmation status.
- **Dependencies:** Local Ticket Management System mockup.

## Proposed Agent Tools

All three proposed functions are exposed as LLM-callable tools:

1. `get_order_status`:
   - **Why exposed:** Allows the agent to query external order systems autonomously when customers inquire about shipping or package status.
2. `search_faq`:
   - **Why exposed:** Enables the agent to retrieve official, grounded store policies rather than hallucinating rules.
3. `create_support_ticket`:
   - **Why exposed:** Provides a fallback mechanism for the agent to escalate unresolved, angry, or complex requests to human operators.

## Model Selection

OpenAI API using `gpt-4o-mini` with native Function Calling capabilities via the official Python `openai` SDK.

## Architecture

```text
[User Input]
     │
     ▼
[LLM Agent Core] ──(System Prompt & Tool Definitions)
     │
     ├──> [Decision: Tool Selection]
     │          │
     │          ├──> `get_order_status(order_id)` ──> [Order Mock DB]
     │          ├──> `search_faq(query)`           ──> [FAQ Knowledge Base]
     │          └──> `create_support_ticket(...)`  ──> [Ticket System DB]
     │
     ▼
[Tool Execution & Argument Validation (Pydantic)]
     │
     ▼
[LLM Response Generation] ──> [Tool-Grounded Output to User] 
```
## Example Requests

1. **Order Status Inquiry:**
   *"Hi, can you tell me where my package is? My order ID is ORD-1001."*
2. **Policy Consultation:**
   *"What is your return policy if I opened the original package 10 days ago?"*
3. **Complex Issue / Human Escalation:**
   *"My order arrived damaged, and I need a refund immediately! Transfer me to a human manager."*

## Evaluation Plan

- Automated unit testing suite using `pytest` with at least 8 test cases covering:
  - Correct tool selection based on user prompt context.
  - Validation of input arguments (e.g., verifying valid order ID formats).
  - Accurate tool-grounded answer generation without hallucination.
  - Proper execution of the human escalation fallback (`create_support_ticket`).
  - Handling of edge cases and failed tool calls (e.g., missing order IDs or database errors).
- Automated repo validation via `npm run validate`.

## Weekly Milestones

- **Week 10 (2026-11-02 – 2026-11-08):** Proposal submission, repository fork configuration, environment setup.
- **Week 11 (2026-11-09 – 2026-11-15):** Setup Python environment, integrate OpenAI API SDK, implement initial LLM response prototype.
- **Week 12 (2026-11-16 – 2026-11-22):** Implement mock order and FAQ databases, add Pydantic schemas for input/output validation.
- **Week 13 (2026-11-23 – 2026-11-29):** Implement `get_order_status`, `search_faq`, and `create_support_ticket` as LLM-callable tools.
- **Week 14 (2026-11-30 – 2026-12-06):** Complete end-to-end tool calling agent workflow and tool error handling logic.
- **Week 15 (2026-12-07 – 2026-12-13):** Add logging, argument bounds checking, execution tracing, and failure recovery mechanisms.
- **Week 16 (2026-12-14 – 2026-12-20):** Implement and execute the full test suite (`pytest`, 8+ tests), record test results in `reports/week-16.md`.
- **Week 17 (2026-12-21 – 2026-12-22):** Final documentation review, record final commit hash, freeze code, and prepare for project defense.