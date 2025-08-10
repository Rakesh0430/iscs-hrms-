import uuid
from sqlalchemy import (
    Column,
    String,
    Date,
    Boolean,
    Text,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255))
    last_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(50))
    blood_group = Column(String(10))
    nationality = Column(String(255))
    marital_status = Column(String(50))
    marriage_date = Column(Date)
    career_ambition = Column(Text)
    significant_achievements = Column(Text)
    professional_failures = Column(Text)
    strengths = Column(ARRAY(String))
    weaknesses = Column(ARRAY(String))
    referred_by_employee = Column(Boolean, default=False)
    referrer_name = Column(String(255))
    referrer_contact_no = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    contacts = relationship(
        "EmployeeContact", back_populates="employee", cascade="all, delete-orphan"
    )
    addresses = relationship(
        "EmployeeAddress", back_populates="employee", cascade="all, delete-orphan"
    )


class EmployeeContact(Base):
    __tablename__ = "employee_contacts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id"), nullable=False)
    mobile_phone_no = Column(String(20))
    email_id = Column(String(255), unique=True, index=True)
    telephone_no = Column(String(20))

    employee = relationship("Employee", back_populates="contacts")


class EmployeeAddress(Base):
    __tablename__ = "employee_addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id"), nullable=False)
    address_type = Column(String(50), nullable=False)  # 'current' or 'permanent'
    city = Column(String(255), nullable=False)
    district = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    pin_code = Column(String(10), nullable=False)

    employee = relationship("Employee", back_populates="addresses")
