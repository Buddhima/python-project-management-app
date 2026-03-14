from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class ClientBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Client or company name"
    )

    email: EmailStr = Field(
        ...,
        description="Primary contact email"
    )

    phone: Optional[str] = Field(
        None,
        max_length=20,
        description="Contact phone number"
    )

    company: Optional[str] = Field(
        None,
        max_length=200,
        description="Company name if different from client name"
    )

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=200,
        description="Updated client or company name"
    )

    email: Optional[EmailStr] = Field(
        None,
        description="Updated primary contact email"
    )

    phone: Optional[str] = Field(
        None,
        max_length=20,
        description="Updated contact phone number"
    )

    company: Optional[str] = Field(
        None,
        max_length=200,
        description="Updated company name if different from client name"
    )


class ClientResponse(ClientBase):
    id: int = Field(
        ...,
        description="Unique identifier of the client"
    )

    created_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the client record was created"
    )

    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the client record was last updated"
    )

    class Config:
        from_attributes = True