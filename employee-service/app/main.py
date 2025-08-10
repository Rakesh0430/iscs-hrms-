from fastapi import FastAPI

from app.api.endpoints import employees

app = FastAPI(
    title="HRMS - Employee Service",
    description="Manages core employee data, including personal information, addresses, and contact details.",
    version="0.1.0",
)


@app.get("/", tags=["Health Check"])
def read_root():
    """
    Health check endpoint to ensure the service is running.
    """
    return {"status": "ok", "message": "Employee Service is running"}


app.include_router(
    employees.router,
    prefix="/api/v1/employees",
    tags=["Employees"],
)
