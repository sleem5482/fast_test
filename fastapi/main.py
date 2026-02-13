from fastapi import Depends, FastAPI
from typing import Annotated
from sqlalchemy.orm import session
from pydantic import BaseModel
from database import sessionLocal,Base,engine
import models
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=['*'],
    allow_headers=['*']
)

class transaction(BaseModel):
    description:str
    amount:float
    category:str
    is_income:bool
    date:str


class transaction_model(transaction):
    id:int

    class Config:
        orm_mode=True
        
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependences=Annotated[session,Depends(get_db)]
models.Base.metadata.create_all(bind=engine)



@app.post("/transactions/",response_model=transaction_model)
async def create_transaction(transaction:transaction,db:db_dependences):
    db_transaction=models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction




@app.get("/transactions/",response_model=list[transaction_model])
async def get_transactions(db:db_dependences,skip:int=0,limit:int=100):
    result=db.query(models.Transaction).offset(skip).limit(limit).all()
    return result