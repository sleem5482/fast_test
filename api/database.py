from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


url_db="postgresql://postgres:sleem5482@localhost:5432/finance"
engine=create_engine(url_db)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()