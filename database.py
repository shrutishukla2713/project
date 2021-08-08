import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,String, create_engine

Base = declarative_base()
class Past_data(Base):
    __tablename__= "Pdata"

    id= Column(Integer,autoincrement=True,primary_key=True)
    country=Column(String)
    last_update=Column(Integer)
    new_cases = Column(Integer)
    new_Deaths=Column(Integer)
    active_cases=Column(Integer)
    total_Recovered=Column(Integer)
    total_Deaths=Column(Integer)
    total_cases=Column(Integer)
    

if __name__=="__main__":
    engine=create_engine("sqlite:///Past_data.sqlite3")
    Base.metadata.create_all(engine)
