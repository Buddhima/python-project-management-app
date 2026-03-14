from app.schemas.report_schema import OutstandingBalanceReport
from datetime import datetime
from typing import List

def outstanding_balance() -> List[OutstandingBalanceReport]:
    now = datetime.utcnow()

    return [
        OutstandingBalanceReport(
            client_id=1,
            client_name="Acme Corporation",
            project_id=101,
            project_name="Website Redesign",
            total_invoiced=15000.0,
            total_paid=9000.0,
            outstanding_balance=6000.0,
            last_payment_date=datetime(2026, 2, 10, 14, 30),
            report_generated_at=now
        ),
        OutstandingBalanceReport(
            client_id=2,
            client_name="Global Tech Ltd",
            project_id=202,
            project_name="Mobile App Development",
            total_invoiced=30000.0,
            total_paid=12000.0,
            outstanding_balance=18000.0,
            last_payment_date=datetime(2026, 1, 25, 9, 15),
            report_generated_at=now
        ),
        OutstandingBalanceReport(
            client_id=3,
            client_name="Bright Marketing",
            project_id=None,
            project_name=None,
            total_invoiced=8000.0,
            total_paid=5000.0,
            outstanding_balance=3000.0,
            last_payment_date=None,
            report_generated_at=now
        )
    ]