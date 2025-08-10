from typing import List, Optional
import uuid

from sqlalchemy.orm import Session

from app.models.employee import Employee, EmployeeContact, EmployeeAddress
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def get_employee(db: Session, employee_id: uuid.UUID) -> Optional[Employee]:
    """
    Get an employee by their primary key ID.
    """
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employee_by_employee_id(db: Session, employee_id: str) -> Optional[Employee]:
    """
    Get an employee by their company-assigned employee_id.
    """
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    """
    Get a list of employees with pagination.
    """
    return db.query(Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: EmployeeCreate) -> Employee:
    """
    Create a new employee, along with their contacts and addresses.
    """
    # Create the main employee record
    db_employee = Employee(
        employee_id=employee.employee_id,
        first_name=employee.first_name,
        middle_name=employee.middle_name,
        last_name=employee.last_name,
        date_of_birth=employee.date_of_birth,
        gender=employee.gender,
        blood_group=employee.blood_group,
        nationality=employee.nationality,
        marital_status=employee.marital_status,
        marriage_date=employee.marriage_date,
        career_ambition=employee.career_ambition,
        significant_achievements=employee.significant_achievements,
        professional_failures=employee.professional_failures,
        strengths=employee.strengths,
        weaknesses=employee.weaknesses,
        referred_by_employee=employee.referred_by_employee,
        referrer_name=employee.referrer_name,
        referrer_contact_no=employee.referrer_contact_no,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    # Create associated contacts and addresses
    for contact_data in employee.contacts:
        db_contact = EmployeeContact(**contact_data.model_dump(), employee_id=db_employee.id)
        db.add(db_contact)

    for address_data in employee.addresses:
        db_address = EmployeeAddress(**address_data.model_dump(), employee_id=db_employee.id)
        db.add(db_address)

    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(
    db: Session, *, db_employee: Employee, employee_in: EmployeeUpdate
) -> Employee:
    """
    Update an employee's details.
    """
    update_data = employee_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_employee, field, value)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: uuid.UUID) -> Optional[Employee]:
    """
    Delete an employee.
    """
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
