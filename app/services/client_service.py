from app.schemas.client_schema import ClientCreate, ClientResponse
from datetime import datetime
import random
from typing import List, Optional


clients: List[ClientResponse] = [
    ClientResponse(
        id=1,
        name="Alice",
        email="alice@gmail.com",
        phone=None,
        company=None,
        created_at=datetime.utcnow(),
        updated_at=None
    ),
    ClientResponse(
        id=2,
        name="Bob",
        email="bob@gmail.com",
        phone="0211234567",
        company="Bob Consulting",
        created_at=datetime.utcnow(),
        updated_at=None
    )
]

def get_all_clients() -> List[ClientResponse]:
    """Return all clients"""
    return clients

def get_client_by_id(client_id: int) -> Optional[ClientResponse]:
    """Find a client by ID"""
    for client in clients:
        if client.id == client_id:
            return client
    return None

def create_client(client: ClientCreate) -> ClientResponse:
    """Create a new client"""
    new_client = ClientResponse(
        id=random.randint(100, 999),
        created_at=datetime.utcnow(),
        updated_at=None,
        **client.model_dump()
    )
    clients.append(new_client)
    return new_client
