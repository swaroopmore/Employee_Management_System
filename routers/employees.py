from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal
import crud

router = APIRouter()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add Employee
@router.post("/add-employee")
def add_employee(
    name: str = Form(...),
    age: int = Form(...),
    department: str = Form(...),
    salary: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_employee(
        db,
        name,
        age,
        department,
        salary
    )

    # Redirect to View Employees page
    return RedirectResponse(
        url="/view-employees",
        status_code=303
    )

@router.get("/delete-employee/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    crud.delete_employee(db, emp_id)

    return RedirectResponse(
        url="/view-employees",
        status_code=303
    )


from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


# Show Edit Form
@router.get("/edit-employee/{emp_id}")
def edit_employee_page(
    request: Request,
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee_by_id(db, emp_id)

    return templates.TemplateResponse(
        request=request,
        name="update_employee.html",
        context={
            "employee": employee
        }
    )


# Update Employee
@router.post("/edit-employee/{emp_id}")
def update_employee(
    emp_id: int,
    name: str = Form(...),
    age: int = Form(...),
    department: str = Form(...),
    salary: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.update_employee(
        db,
        emp_id,
        name,
        age,
        department,
        salary
    )

    return RedirectResponse(
        url="/view-employees",
        status_code=303
    )