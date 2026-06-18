from fastapi import APIRouter, Depends,Form,HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import auth

import crud
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    username: str=Form(...),
    email: str=Form(...),
    password: str=Form(...),
    db: Session = Depends(get_db)
):
    crud.create_user(db, username, email, password)

    # Redirect to login page after registration
    return RedirectResponse(
        url="/login",
        status_code=303
    )



@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_username(db, username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not auth.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )