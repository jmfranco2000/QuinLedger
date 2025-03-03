from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.payments import Payment
from models.users import User  # 📌 Importamos User
from schemas import PaymentCreate, PaymentResponse
from typing import List

router = APIRouter()

# 📌 Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Crear un nuevo pago (asociado a un usuario)
@router.post("/api/payments/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payment.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    # 📌 Retornamos un diccionario con los datos correctos
    return {
        "id": db_payment.id,
        "user_id": db_payment.user_id,
        "name": db_payment.name,
        "amount": db_payment.amount,
        "fixed": db_payment.fixed,
        "due_date": db_payment.due_date,
        "paid": db_payment.paid
    }


