import uuid
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, ConfigDict


# Schemas for EmployeeContact
class EmployeeContactBase(BaseModel):
    mobile_phone_no: Optional[str] = None
    email_id: Optional[EmailStr] = None
    telephone_no: Optional[str] = None


class EmployeeContactCreate(EmployeeContactBase):
    email_id: EmailStr  # Make email required for new contacts


class EmployeeContactUpdate(EmployeeContactBase):
    pass


class EmployeeContactRead(EmployeeContactBase):
    id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)


# Schemas for EmployeeAddress
class EmployeeAddressBase(BaseModel):
    address_type: str
    city: str
    district: str
    state: str
    pin_code: str


class EmployeeAddressCreate(EmployeeAddressBase):
    pass


class EmployeeAddressUpdate(BaseModel):
    address_type: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    pin_code: Optional[str] = None


class EmployeeAddressRead(EmployeeAddressBase):
    id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)


# Schemas for Employee
class EmployeeBase(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    date_of_birth: date
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    nationality: Optional[str] = None
    marital_status: Optional[str] = None
    marriage_date: Optional[date] = None
    career_ambition: Optional[str] = None
    significant_achievements: Optional[str] = None
    professional_failures: Optional[str] = None
    strengths: Optional[List[str]] = None
    weaknesses: Optional[List[str]] = None
    referred_by_employee: bool = False
    referrer_name: Optional[str] = None
    referrer_contact_no: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    employee_id: str
    contacts: List[EmployeeContactCreate] = []
    addresses: List[EmployeeAddressCreate] = []


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    nationality: Optional[str] = None
    marital_status: Optional[str] = None
    marriage_date: Optional[date] = None
    career_ambition: Optional[str] = None
    significant_achievements: Optional[str] = None
    professional_failures: Optional[str] = None
    strengths: Optional[List[str]] = None
    weaknesses: Optional[List[str]] = None
    referred_by_employee: Optional[bool] = None
    referrer_name: Optional[str] = None
    referrer_contact_no: Optional[str] = None


class EmployeeRead(EmployeeBase):
    id: uuid.UUID
    employee_id: str
    created_at: datetime
    updated_at: datetime
    contacts: List[EmployeeContactRead] = []
    addresses: List[EmployeeAddressRead] = []
    model_config = ConfigDict(from_attributes=True)
