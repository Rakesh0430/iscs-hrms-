from typing import List, Any
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app import crud
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.EmployeeRead)
def create_employee(
    *,
    db: Session = Depends(get_db),
    employee_in: schemas.EmployeeCreate,
) -> Any:
    """
    Create new employee.
    """
    employee = crud.get_employee_by_employee_id(db, employee_id=employee_in.employee_id)
    if employee:
        raise HTTPException(
            status_code=400,
            detail=f"The employee with employee_id '{employee_in.employee_id}' already exists.",
        )
    employee = crud.create_employee(db=db, employee=employee_in)
    return employee


@router.get("/", response_model=List[schemas.EmployeeRead])
def read_employees(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve employees.
    """
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@router.get("/{employee_id}", response_model=schemas.EmployeeRead)
def read_employee(
    *,
    db: Session = Depends(get_db),
    employee_id: uuid.UUID,
) -> Any:
    """
    Get employee by ID.
    """
    employee = crud.get_employee(db, employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=schemas.EmployeeRead)
def update_employee(
    *,
    db: Session = Depends(get_db),
    employee_id: uuid.UUID,
    employee_in: schemas.EmployeeUpdate,
) -> Any:
    """
    Update an employee.
    """
    employee = crud.get_employee(db, employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee = crud.update_employee(db=db, db_employee=employee, employee_in=employee_in)
    return employee


@router.delete("/{employee_id}", response_model=schemas.EmployeeRead)
def delete_employee(
    *,
    db: Session = Depends(get_db),
    employee_id: uuid.UUID,
) -> Any:
    """
    Delete an employee.
    """
    employee = crud.get_employee(db, employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee = crud.delete_employee(db=db, employee_id=employee_id)
    return employee
