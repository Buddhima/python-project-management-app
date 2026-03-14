from fastapi import Depends
from app.services import client_service, invoice_service, project_service, report_service, user_service

def get_client_service():
    """Dependency injection for ClientService"""
    return client_service

def get_invoice_service():
    """Dependency injection for InvoiceService"""
    return invoice_service

def get_project_service():
    """Dependency injection for ProjectService"""
    return project_service

def get_report_service():
    """Dependency injection for ReportService"""
    return report_service

def get_user_service():
    """Dependency injection for UserService"""
    return user_service