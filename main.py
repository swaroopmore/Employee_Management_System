from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from routers.users import router as user_router
from database import engine
from models import Base
from routers import employees

app = FastAPI()
app.include_router(user_router)
app.include_router(employees.router)

# Create database tables
Base.metadata.create_all(bind=engine)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
#Without this your css wont load

# Templates folder
templates = Jinja2Templates(directory="templates")#This tells fastapi where your HTML files are stored


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

@app.get("/dashboard",response_class=HTMLResponse)
def dashboard(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )

from database import SessionLocal
import crud

@app.get("/view-employees", response_class=HTMLResponse)
def view_employees(request: Request):
    db = SessionLocal()

    employees = crud.get_all_employees(db)

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="view_employee.html",
        context={
            "employees": employees
        }
    )

@app.get("/add-employee", response_class=HTMLResponse)
def add_employee_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_employee.html"
    )