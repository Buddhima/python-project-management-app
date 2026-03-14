from fastapi import APIRouter, Query, Path, Depends
from fastapi import HTTPException, status
from typing import List, Optional
from app.schemas.project_schema import ProjectCreate, ProjectResponse
from app.schemas.error_schema import ErrorResponse
from app.auth import get_current_user
from app.dependencies.services import get_project_service

router = APIRouter(
    prefix="/projects", 
    tags=["Projects"],
    dependencies=[Depends(get_current_user)]
)

@router.get(
    "/",
    response_model=List[ProjectResponse]
)
def get_projects(client_id: Optional[int] = Query(None), service=Depends(get_project_service)) -> List[ProjectResponse]:
    """Retrieve all clients, optionally filter by client_id"""
    return service.get_all_projects(client_id=client_id)

@router.get(
    "/{project_id}",
    responses={
        404: {"model": ErrorResponse, "description": "Item not found"}
    },
    response_model=ProjectResponse
)
def get_project(project_id: int = Path(...), service=Depends(get_project_service)) -> ProjectResponse:
    """Retrieve a project by id"""
    project = service.get_project_by_id(project_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found"
        )

    return project

@router.post(
    "/",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid item details"},
    },
    response_model=ProjectResponse
)
def add_project(project: ProjectCreate, service=Depends(get_project_service)) -> ProjectResponse:
    """Adding a new project"""
    try:
        return service.create_project(project)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))