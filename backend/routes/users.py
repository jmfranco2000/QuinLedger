from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import User  # Importa el modelo SQLAlchemy
from database import get_db
from schemas import UserCreate, UserResponse  # Importa los esquemas Pydantic

router = APIRouter()

@router.post("/api/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user  # Devuelve el usuario recién creado
