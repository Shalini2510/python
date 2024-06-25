# first install sqlalchemy from cmd --> python -m pip install sqlalchemy

from urllib.parse import quote_plus
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base

Base= declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id= Column(Integer, primary_key=True)
    customername=Column(String(50))
    customeremail=Column(String(50))

    def __repr__(self):
        return f"Name:{self.customername},Email:{self.customeremail}"

engine = create_engine("mysql+pymysql://root:%s@localhost:3306/demodb_2" %quote_plus("rps@123"))

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

session =sessionmaker(bind=engine)
dbsession=session()

#INSERT DATA

#customer= Customer(customername='abc company', customeremail='abc@example.com')  #insert record in table customer 

#dbsession.add(customer)
#dbsession.commit()


#RETRIEVE DATA

records=dbsession.query(Customer).all()   #equivalent to quer select * from customer
print(records)