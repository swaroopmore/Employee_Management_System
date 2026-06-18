from pydantic import BaseModel

# ---------- User Schemas ----------

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# ---------- Employee Schemas ----------

class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str
    salary: int

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    department: str
    salary: int

    class Config:
        from_attributes = True