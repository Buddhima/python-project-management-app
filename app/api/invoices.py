from fastapi import APIRouter, Query, Path, Depends, HTTPException
from typing import List, Optional
from app.schemas.invoice_schema import InvoiceStatusUpdate, InvoiceStatus, InvoiceResponse, InvoiceCreate
from app.schemas.adjustment_schema import Adjustment, AdjustmentResponse
from app.schemas.user_schema import LoginUser, UserRole
from app.auth import RoleChecker, get_current_user
from app.schemas.error_schema import ErrorResponse
from app.dependencies.services import get_invoice_service

router = APIRouter(
    prefix="/invoices", 
    tags=["Invoices"], 
    dependencies=[Depends(get_current_user)]
)

# Initialize the checker for Managers
allow_manager = RoleChecker(allowed_roles=[UserRole.MANAGER])

@router.get(
    "/",
    response_model=List[InvoiceResponse]
)
def get_invoices(project_id: Optional[int] = Query(None), status: Optional[str] = Query(None), service=Depends(get_invoice_service)) -> List[InvoiceResponse]:
    """Retrieve all invoices, can be filtered by project_id or status"""
    return service.get_all_invoices(project_id=project_id, status=status)

@router.get(
    "/{invoice_id}", 
    responses={
        404: {"model": ErrorResponse, "description": "Item not found"}
    },
    response_model=InvoiceResponse
)
def get_invoice(invoice_id: int = Path(...), service=Depends(get_invoice_service)) -> InvoiceResponse:
    """Retrieve invoice by id"""
    return service.get_invoice_by_id(invoice_id)

@router.post(
    "/",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
    },
    response_model=InvoiceResponse
)
def add_invoice(invoice: InvoiceCreate, service=Depends(get_invoice_service)) -> InvoiceResponse:
    """Adding a new invoice"""
    try:
        return service.create_invoice(invoice)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post(
    "/{invoice_id}/adjustments",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
    },
    response_model=AdjustmentResponse
)
def add_invoice_adjustment(adjustment: Adjustment, invoice_id: int = Path(...), service=Depends(get_invoice_service)) -> AdjustmentResponse:
    """Adding a new invoice adjustment"""
    return service.add_adjustment(invoice_id, adjustment)

# Sample invoice workflow: draft-> approved -> sent -> paid

@router.post(
    "/{invoice_id}/approve",
    dependencies=[Depends(allow_manager)],
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
        403: {"model": ErrorResponse, "description": "Operation not permitted"},
    }
)
def approve_invoice(invoice_id: int = Path(...), current_user: LoginUser = Depends(RoleChecker([UserRole.MANAGER])), service=Depends(get_invoice_service)) -> bool:
    """Approving an invoice \n
    🔒 **Restricted:** Only accessible by users with the 'manager' role."""
    return service.approve_invoice(invoice_id)

@router.post("/{invoice_id}/send")
def send_invoice(invoice_id: int = Path(...), service=Depends(get_invoice_service)) -> bool:
    """Sending an invoice"""
    return service.send_invoice(invoice_id)

@router.post("/{invoice_id}/pay")
def pay_invoice(invoice_id: int = Path(...), service=Depends(get_invoice_service)) -> bool:
    """Mark an invoice paid"""
    return service.pay_invoice(invoice_id)

# Generic way to handle the workflow

@router.put(
    "/{invoice_id}/status",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
        403: {"model": ErrorResponse, "description": "Operation not permitted"},
    }
)
def update_invoice_status(payload: InvoiceStatusUpdate, invoice_id: int = Path(...), current_user: LoginUser = Depends(get_current_user), service=Depends(get_invoice_service)) -> bool:
    """Updating an invoice status"""
    if (payload.new_status == InvoiceStatus.APPROVED):
        if(current_user.role == UserRole.MANAGER):
            return service.approve_invoice(invoice_id)
        else:
            raise HTTPException(status_code=403, detail="Operation not permitted")
    else:
        return service.update_invoice_status(invoice_id, payload)