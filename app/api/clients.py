from fastapi import APIRouter, Path, Depends
from fastapi import HTTPException, status
from typing import List
from app.schemas.client_schema import ClientCreate, ClientResponse
from app.schemas.error_schema import ErrorResponse
from app.auth import get_current_user
from app.dependencies.services import get_client_service

router = APIRouter(
    prefix="/clients", 
    tags=["Clients"], 
    dependencies=[Depends(get_current_user)]
)

@router.get(
    "/",
    response_model=List[ClientResponse]
)
def get_clients(service=Depends(get_client_service)) -> List[ClientResponse]:
    """Retrieve all clients"""
    return service.get_all_clients()

@router.get(
    "/{client_id}",
    responses={
        404: {"model": ErrorResponse, "description": "Item not found"}
    },
    response_model=ClientResponse
)
def get_client(client_id: int = Path(...), service=Depends(get_client_service)) -> ClientResponse:
    """Retrieve client by id"""
    client = service.get_client_by_id(client_id)

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with id {client_id} not found"
        )
    return client

@router.get(
    "/{client_id}/history",
    responses={
        404: {"model": ErrorResponse, "description": "Item not found"}
    },
    response_model=ClientResponse
)
def get_client_history(client_id: int = Path(...), service=Depends(get_client_service)) -> ClientResponse:
    """Retrieve client history"""
    return service.get_client_history_by_id(client_id)

@router.post(
    "/",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
    },
    response_model=ClientResponse
)
def add_client(client: ClientCreate, service=Depends(get_client_service)) -> ClientResponse:
    """Adding a new client"""
    try:
        return service.create_client(client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
