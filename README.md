# Project Management API

## 🚀 Overview

A robust Project Management API designed to simplify and automate the full project lifecycle. This API allows seamless management of clients, projects, and invoices, supporting business workflows such as billing, adjustments, reporting, and approval processes.

## 🛠️ Key Modules

- **Clients** – Manage client relationships, details, and associated projects.
- **Projects** – Full CRUD support to manage project lifecycle per client.
- **Invoices** – Automated invoice generation and tracking with support for multiple invoices per project. Handles pending, sent, and paid states, as well as adjustments and credits.

## 🎯 Features

- Manage clients and their projects.
- Generate and manage invoices, including multiple invoices per project.
- Support invoice states: Pending, Sent, Paid.
- Apply adjustments or credits to invoices.
- Approval workflow for invoices: staff create/manage, managers approve/report.
- Pull financial reports on outstanding balances and billing history.
- Role-based user management: Staff and Managers with separate permissions.

## ⚙️ Setup Instructions
1. Create Environment
```
python3 -m venv venv
source venv/bin/activate
```
2. Install Dependencies
```
pip install -r requirements.txt
````
3. Run the Server
```
uvicorn app.main:app --reload
```

## 📄 API Documentation

Once the server is running, access the interactive API docs at:

http://127.0.0.1:8000/docs

or the alternative ReDoc interface:

http://127.0.0.1:8000/redoc

## 👥 Users & Roles

- Staff: Create and manage invoices.
- Managers: Approve invoices, generate reports, and oversee financial workflows.

## 📊 Reporting

The API supports pulling reports on:
- Outstanding balances per client or project.
- Billing history across selected periods.
- Status of invoices (pending, sent, paid) including adjustments and credits applied.

## 📧 Contact

For support or queries, reach out to:

Name: Senior Developer

Email: support@bdo.nz

Website: https://bdo.nz/support

## 📄 License

This project is licensed under the MIT License.

License: MIT

URL: https://opensource.org/licenses/MIT

## 🔗 Quick Start Summary

- Create a virtual environment.
- Install dependencies.
- Run the server with `uvicorn app.main:app --reload`.
- Use API documentation to interact with Clients, Projects, and Invoices endpoints.
