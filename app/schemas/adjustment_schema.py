from pydantic import BaseModel, Field

class Adjustment(BaseModel):
    amount: float
    reason: str

class AdjustmentResponse(Adjustment):
    invoice_id: int = Field(
        ...,
        description="Unique identifier of the invoice."
    )