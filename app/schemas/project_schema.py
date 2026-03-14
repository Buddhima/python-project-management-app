from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ProjectBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Human-readable name of the project."
    )

    description: Optional[str] = Field(
        None,
        max_length=2000,
        description="Detailed description outlining the project goals, scope, and deliverables."
    )

    client_id: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the client who owns or requested the project."
    )

    status: ProjectStatus = Field(
        default=ProjectStatus.PLANNING,
        description="Current lifecycle status of the project (e.g., planning, active, completed)."
    )

    budget: Optional[float] = Field(
        None,
        ge=0,
        description="Total allocated budget for the project in the agreed currency."
    )

    start_date: Optional[datetime] = Field(
        None,
        description="Scheduled start date and time of the project."
    )

    end_date: Optional[datetime] = Field(
        None,
        description="Expected or actual completion date and time of the project."
    )

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int = Field(
        ...,
        description="Unique identifier of the project."
    )

    created_at: datetime = Field(
        ...,
        description="Timestamp when the project record was created."
    )

    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the project record was last updated."
    )

    class Config:
        from_attributes = True