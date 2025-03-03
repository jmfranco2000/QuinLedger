from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Relación con el usuario
    name = Column(String, nullable=False)  # Nombre del pago (Ej: Hipoteca, Luz)
    amount = Column(Float, nullable=False)  # Monto a pagar
    fixed = Column(Boolean, default=True)  # Si el pago es fijo o variable
    due_date = Column(Date, nullable=False)  # Fecha de vencimiento
    paid = Column(Boolean, default=False)  # Si está pagado o no

