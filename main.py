from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.users import User
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:4321"]  # Puerto por defecto de Astro.js

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

# Asegurar que las tablas existen
Base.metadata.create_all(bind=engine)

# Esquema para validación de entrada
class UserCreate(BaseModel):
    name: str
    email: EmailStr  # 👈 Validar que sea un email válido

# Dependencia de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 📌 Verificar si el email ya existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")  # 👈 Evita duplicados
    
    # ✅ Si no existe, crear nuevo usuario
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "User created successfully", "user": db_user}

@app.get("/api/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
