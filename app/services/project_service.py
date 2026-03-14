from typing import List, Optional
from datetime import datetime
import random
from app.schemas.project_schema import ProjectCreate, ProjectResponse, ProjectStatus

projects: List[ProjectResponse] = [
    ProjectResponse(
        id=1,
        name="Project Alpha",
        description="First project",
        client_id=1,
        status=ProjectStatus.ACTIVE,
        budget=10000.0,
        start_date=datetime(2026, 1, 1),
        end_date=None,
        created_at=datetime.utcnow(),
        updated_at=None
    ),
    ProjectResponse(
        id=2,
        name="Project Beta",
        description="Second project",
        client_id=2,
        status=ProjectStatus.PLANNING,
        budget=5000.0,
        start_date=None,
        end_date=None,
        created_at=datetime.utcnow(),
        updated_at=None
    )
]

def get_all_projects(client_id: Optional[int] = None) -> List[ProjectResponse]:
    if client_id is None:
        return projects
    return [p for p in projects if p.client_id == client_id]

def get_project_by_id(project_id: int) -> ProjectResponse:
    for project in projects:
        if project.id == project_id:
            return project

    return None

def create_project(project: ProjectCreate) -> ProjectResponse:
    new_project = ProjectResponse(
        id=random.randint(100, 999),  # unique ID for demo
        created_at=datetime.utcnow(),
        updated_at=None,
        **project.model_dump()
    )
    projects.append(new_project)
    return new_project
