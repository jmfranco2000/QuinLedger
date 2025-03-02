from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.users import User
from pydantic import BaseModel, EmailStr

app = FastAPI()

# 📌 Asegurar que las tablas existen ANTES de usar la API
Base.metadata.create_all(bind=engine)

# 📌 Esquema de validación para usuarios
class UserCreate(BaseModel):
    name: str
    email: EmailStr  # 👈 Validar que sea un email válido

# 📌 Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Endpoint para crear usuarios
@app.post("/api/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "User created successfully", "user": {"id": db_user.id, "name": db_user.name, "email": db_user.email}}

# 📌 Endpoint para listar usuarios
@app.get("/api/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]
