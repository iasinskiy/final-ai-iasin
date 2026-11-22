from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field, field_validator
import re


# --- Входные схемы для валидации аргументов LLM ---

class OrderStatusInput(BaseModel):
    order_id: str = Field(
        ...,
        description="Unique order identifier in format ORD-XXXX (e.g., ORD-1001)"
    )

    @field_validator("order_id")
    @classmethod
    def validate_order_id_format(cls, value: str) -> str:
        cleaned = value.strip().upper()
        if not re.match(r"^ORD-\d{4,}$", cleaned):
            raise ValueError(
                f"Invalid order_id format '{value}'. Expected format like 'ORD-1001'."
            )
        return cleaned


class FAQSearchInput(BaseModel):
    query: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Search keywords or customer policy question"
    )


class SupportTicketInput(BaseModel):
    user_id: str = Field(
        default="GUEST",
        min_length=2,
        max_length=50,
        description="Customer identifier (e.g., USR-501 or GUEST)"
    )
    issue_description: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Detailed summary of the customer's issue requiring human support"
    )
    priority: Literal["low", "medium", "high"] = Field(
        default="medium",
        description="Ticket urgency level: low, medium, or high"
    )


# --- Выходные схемы (структура данных БД и ответов инструментов) ---

class OrderItem(BaseModel):
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(ge=0)


class OrderRecord(BaseModel):
    order_id: str
    user_id: str
    status: Literal["processing", "shipped", "delivered", "cancelled"]
    tracking_number: Optional[str] = None
    items: list[OrderItem]
    estimated_delivery: str


class FAQMatch(BaseModel):
    id: str
    category: str
    question: str
    answer: str
    relevance_score: float = Field(ge=0.0, le=1.0)


class SupportTicketRecord(BaseModel):
    ticket_id: str
    user_id: str
    issue_description: str
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "in_progress", "resolved"] = "open"
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())