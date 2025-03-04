from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine, Base  # Correcto
from backend.models.users import User  # Correcto
from pydantic import BaseModel, EmailStr
from routes.payments import router as payments_router

app = FastAPI()

# Incluir el router de pagos y otras rutas necesarias
app.include_router(payments_router)

# Asegurar que las tablas se creen en la base de datos
Base.metadata.create_all(bind=engine)

# Dependencia para manejar la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Esquema para crear un nuevo usuario
class UserCreate(BaseModel):
    name: str
    email: EmailStr

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

@app.get("/api/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]
