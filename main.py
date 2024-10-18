# Assuming you have a SQLAlchemy session and a customer instance from the database
customer = session.query(Customer).first()

# Convert to Pydantic model
customer_data = CustomerSchema.from_orm(customer)

# Now you can use `customer_data` for validation, serialization, etc.
print(customer_data.json())
