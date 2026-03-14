from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class OutstandingBalanceReport(BaseModel):
    client_id: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the client associated with the outstanding balance."
    )

    client_name: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Human-readable name of the client."
    )

    project_id: Optional[int] = Field(
        None,
        gt=0,
        description="Unique identifier of the project associated with the balance, if applicable."
    )

    project_name: Optional[str] = Field(
        None,
        min_length=3,
        max_length=200,
        description="Human-readable name of the project associated with the outstanding balance."
    )

    total_invoiced: float = Field(
        ...,
        ge=0,
        description="Total amount invoiced to the client or project."
    )

    total_paid: float = Field(
        ...,
        ge=0,
        description="Total amount received from the client."
    )

    outstanding_balance: float = Field(
        ...,
        ge=0,
        description="Remaining unpaid amount calculated as total invoiced minus total paid."
    )

    last_payment_date: Optional[datetime] = Field(
        None,
        description="Date and time of the most recent payment received from the client."
    )

    report_generated_at: datetime = Field(
        ...,
        description="Timestamp when the outstanding balance report was generated."
    )