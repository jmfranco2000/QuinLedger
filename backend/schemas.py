from pydantic import BaseModel
from datetime import date

# 📌 Esquema para crear un pago
class PaymentCreate(BaseModel):
    user_id: int
    name: str
    amount: float
    fixed: bool
    due_date: date

# 📌 Esquema corregido para mostrar un pago
class PaymentResponse(BaseModel):
    id: int
    user_id: int
    name: str
    amount: float
    fixed: bool
    due_date: date
    paid: bool

    class Config:
        from_attributes = True

