from sqlalchemy.orm import Session
import models
import auth


def create_user(db: Session, username: str, email: str, password: str):
    print("Password",repr(password))
    print("Type",type(password))
    print("Length",len(password))
    hashed_password = auth.hash_password(password)

    user = models.User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_username(db: Session, username: str):
    return (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

def get_all_employees(db:Session):
    return db.query(models.Employee).all()

def create_employee(db:Session, name, age, department, salary):
    employee = models.Employee(
        name=name,
        age=age,
        department=department,
        salary=salary
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee

def delete_employee(db:Session, emp_id):
    employee = (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

    if employee:
        db.delete(employee)
        db.commit()

    return employee

def get_employee_by_id(db:Session, emp_id):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def update_employee(db:Session, emp_id, name, age, department, salary):
    employee = get_employee_by_id(db, emp_id)

    if employee:
        employee.name = name
        employee.age = age
        employee.department = department
        employee.salary = salary

        db.commit()
        db.refresh(employee)

    return employee