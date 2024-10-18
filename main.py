from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Date, Numeric, Integer
from pydantic import BaseModel, EmailStr, constr, condecimal
from datetime import date
import pandas as pd
from db.schema import CustomerSchema
# SQLAlchemy engine and session setup
DATABASE_URL = "postgresql://username:password@localhost/dbname"  # Replace with your actual connection string
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Fetch data from PostgreSQL using SQLAlchemy
def fetch_customers_from_db():
    return session.query(Customer).all()

# Convert SQLAlchemy result to Pydantic schema and then to a list of dictionaries
def customers_to_dict_list(customers):
    return [CustomerSchema.from_orm(customer).dict() for customer in customers]

# Fetch customers and export to Excel
def export_to_excel(customers_data):
    df = pd.DataFrame(customers_data)
    df.to_excel("weekly_customer_report.xls", index=False)
    print("Customer report generated successfully as weekly_customer_report.xls")

if __name__ == "__main__":
    # Step 1: Fetch customers from the database
    customers = fetch_customers_from_db()
    
    # Step 2: Convert the data to Pydantic schemas and then to a dictionary list
    customers_data = customers_to_dict_list(customers)
    
    # Step 3: Export the customer data to Excel
    export_to_excel(customers_data)
