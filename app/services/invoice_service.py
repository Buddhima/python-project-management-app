from app.schemas.invoice_schema import InvoiceStatusUpdate, InvoiceResponse, InvoiceStatus, InvoiceCreate
from app.schemas.adjustment_schema import Adjustment, AdjustmentResponse
from datetime import datetime
from typing import List, Optional
from enum import Enum
import random

invoices: List[InvoiceResponse] = [
    InvoiceResponse(
        id=1,
        project_id=1,
        amount=1500.0,
        currency="USD",
        notes="Initial milestone payment",
        status=InvoiceStatus.PENDING,
        created_by=101,
        created_at=datetime(2026, 3, 1, 10, 0),
        updated_at=None
    ),
    InvoiceResponse(
        id=2,
        project_id=1,
        amount=2000.0,
        currency="USD",
        notes="Second milestone",
        status=InvoiceStatus.APPROVED,
        created_by=102,
        created_at=datetime(2026, 3, 5, 15, 30),
        updated_at=datetime(2026, 3, 6, 9, 0)
    ),
    InvoiceResponse(
        id=3,
        project_id=2,
        amount=500.0,
        currency="EUR",
        notes="Initial deposit",
        status=InvoiceStatus.PAID,
        created_by=103,
        created_at=datetime(2026, 2, 20, 14, 0),
        updated_at=datetime(2026, 3, 1, 12, 0)
    ),
]

def get_all_invoices(project_id: Optional[int] = None, status: Optional[str] = None) -> List[InvoiceResponse]:
    """Return all invoices, optionally filtered by project_id and/or status."""
    result = invoices  # the in-memory list of InvoiceResponse
    if project_id is not None:
        result = [inv for inv in result if inv.project_id == project_id]
    if status is not None:
        result = [inv for inv in result if inv.status.value == status]  # status is Enum
    return result

def get_invoice_by_id(invoice_id: int) -> InvoiceResponse:
    for invoice in invoices:
        if invoice.id == invoice_id:
            return invoice

    return None

def create_invoice(invoice: InvoiceCreate) -> InvoiceResponse:
    new_invoice = InvoiceResponse(
        id=random.randint(100, 999),  # generate a unique ID for demo purposes
        status=InvoiceStatus.PENDING,  # default status
        created_at=datetime.utcnow(),
        updated_at=None,
        **invoice.model_dump()  # convert Pydantic model to dict
    )
    invoices.append(new_invoice)
    return new_invoice

def approve_invoice(invoice_id: int):
    return True

def update_invoice_status(invoice_id: int, payload: InvoiceStatusUpdate):
    return True

def add_adjustment(invoice_id: int, adjustment: Adjustment):
    return AdjustmentResponse(
        invoice_id=invoice_id,
        **adjustment.model_dump()
    )
