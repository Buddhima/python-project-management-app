from fastapi import FastAPI
from app.api import clients, invoices, login, projects, reports

app = FastAPI(
    title="Project Management API",
    version="1.0.0",
    description = """
    🚀 Overview
    A robust Project Management API designed for seamless handling of the project lifecycle.

    🛠️ Key Modules
    * Clients: Manage relationships and data.
    * Projects: Full CRUD lifecycle support.
    * Invoices: Automated generation and tracking.
    """,
    contact={
        "name": "Senior Developer",
        "email": "support@bdo.nz",
        "url": "https://bdo.nz/support",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# List of routers to include
routers = [
    login.router,
    clients.router,
    invoices.router,
    projects.router,
    reports.router,
]

for router in routers:
    app.include_router(router)
