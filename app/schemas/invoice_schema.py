from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class InvoiceBase(BaseModel):
    project_id: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the project associated with this invoice."
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Total monetary amount to be billed for the invoice."
    )

    currency: str = Field(
        default="USD",
        min_length=3,
        max_length=3,
        description="ISO currency code used for the invoice amount (e.g., USD, NZD, EUR)."
    )

    notes: Optional[str] = Field(
        None,
        max_length=1000,
        description="Optional notes or comments providing additional invoice details."
    )

class InvoiceCreate(InvoiceBase):
    created_by: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the user who created the invoice."
    )

class InvoiceUpdate(BaseModel):
    amount: Optional[float] = Field(
        None,
        gt=0,
        description="Updated invoice amount."
    )

    currency: Optional[str] = Field(
        None,
        min_length=3,
        max_length=3,
        description="Updated ISO currency code."
    )

    notes: Optional[str] = Field(
        None,
        max_length=1000,
        description="Updated notes or additional invoice details."
    )

class InvoiceStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    PAID = "paid"

class InvoiceStatusUpdate(BaseModel):
    new_status: InvoiceStatus = Field(
        ...,
        description="New status to assign to the invoice."
    )

    notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional explanation or audit note for the status change."
    )

class InvoiceResponse(InvoiceBase):
    id: int = Field(
        ...,
        description="Unique identifier of the invoice."
    )

    status: InvoiceStatus = Field(
        ...,
        description="Current processing status of the invoice."
    )

    created_by: int = Field(
        ...,
        description="User ID of the person who created the invoice."
    )

    created_at: datetime = Field(
        ...,
        description="Timestamp when the invoice was created."
    )

    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the invoice was last modified."
    )

    class Config:
        from_attributes = True