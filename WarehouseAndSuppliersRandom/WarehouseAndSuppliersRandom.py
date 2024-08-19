import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate random warehouse data
def generate_warehouse_data(num_records):
    data = []
    for _ in range(num_records):
        warehouse_id = fake.unique.random_int(min=100000, max=999999)
        warehouse_name = fake.company()
        location = fake.city()
        capacity = fake.random_int(min=1000, max=50000)
        
        data.append([warehouse_id, warehouse_name, location, capacity])
    
    df = pd.DataFrame(data, columns=['WarehouseID', 'WarehouseName', 'Location', 'Capacity'])
    return df

# Function to generate random supplier data
def generate_supplier_data(num_records):
    data = []
    for _ in range(num_records):
        supplier_id = fake.unique.random_int(min=100000, max=999999)
        supplier_name = fake.company()
        contact_name = fake.name()
        phone_number = fake.phone_number()
        email = fake.email()
        address = fake.address().replace("\n", ", ")
        city = fake.city()
        state = fake.state()
        zip_code = fake.zipcode()
        country = fake.country()
        
        data.append([supplier_id, supplier_name, contact_name, phone_number, email, address, city, state, zip_code, country])
    
    df = pd.DataFrame(data, columns=['SupplierID', 'SupplierName', 'ContactName', 'PhoneNumber', 'Email', 'Address', 'City', 'State', 'ZipCode', 'Country'])
    return df

# Function to generate random inventory data
def generate_inventory_data(num_records):
    data = []
    for _ in range(num_records):
        inventory_id = fake.unique.random_int(min=100000, max=999999)
        warehouse_id = fake.random_int(min=100000, max=999999)
        product_id = fake.random_int(min=100000, max=999999)
        quantity_on_hand = fake.random_int(min=0, max=500)
        last_restocked = fake.date_between(start_date='-2y', end_date='today')
        
        data.append([inventory_id, warehouse_id, product_id, quantity_on_hand, last_restocked])
    
    df = pd.DataFrame(data, columns=['InventoryID', 'WarehouseID', 'ProductID', 'QuantityOnHand', 'LastRestocked'])
    return df

# Generating datasets for each table
warehouse_df = generate_warehouse_data(5)
supplier_df = generate_supplier_data(50)
inventory_df = generate_inventory_data(500)

# Saving datasets to CSV files
warehouse_df.to_csv('warehouses.csv', index=False)
supplier_df.to_csv('suppliers.csv', index=False)
inventory_df.to_csv('inventory.csv', index=False)

print("Data generation complete. CSV files saved.")
