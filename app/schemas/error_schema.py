from pydantic import BaseModel
from typing import Optional

class ErrorResponse(BaseModel):
    detail: str  # short error message
    code: Optional[int] = None  # optional error code
    extra: Optional[dict] = None  # optional extra info