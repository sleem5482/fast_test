from database import Base
from sqlalchemy import Column,Integer,String,Float,Boolean

class Transaction(Base):
    __tablename__="transactions"
    id=Column(Integer,primary_key=True,index=True)
    description=Column(String)
    amount=Column(Float)
    category=Column(String)
    is_income =Column(Boolean)
    date= Column(String)