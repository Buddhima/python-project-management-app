from fastapi import APIRouter, Query, Path, Depends
from typing import List
from app.schemas.report_schema import OutstandingBalanceReport
from app.schemas.user_schema import LoginUser, UserRole
from app.auth import RoleChecker, get_current_user
from app.dependencies.services import get_report_service

router = APIRouter(
    prefix="/reports", 
    tags=["Reports"], 
    dependencies=[Depends(get_current_user)]
)

@router.get(
    "/outstanding-balances",
    response_model=List[OutstandingBalanceReport]
)
def generate_outstanding_balance_report(current_user: LoginUser = Depends(RoleChecker([UserRole.MANAGER])), service=Depends(get_report_service)) -> List[OutstandingBalanceReport]:
    """Retrieve outstanding balance report"""
    return service.outstanding_balance()