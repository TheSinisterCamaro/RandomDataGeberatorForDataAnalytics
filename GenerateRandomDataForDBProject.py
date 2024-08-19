import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate random employee data
def generate_employee_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        employee_id = fake.unique.random_int(min=100000, max=999999)
        if employee_id not in used_ids:
            used_ids.add(employee_id)
            first_name = fake.first_name()
            last_name = fake.last_name()
            dob = fake.date_of_birth(minimum_age=22, maximum_age=65)
            gender = random.choice(['M', 'F'])
            department = random.choice(['IT', 'HR', 'Sales', 'Finance', 'Marketing', 'Support'])
            hire_date = fake.date_between(start_date='-15y', end_date='today')
            salary = round(random.uniform(50000, 150000), 2)
            email = fake.email()
            phone_number = fake.phone_number()

            data.append([employee_id, first_name, last_name, dob, gender, department, hire_date, salary, email, phone_number])

    df = pd.DataFrame(data, columns=['EmployeeID', 'FirstName', 'LastName', 'DOB', 'Gender', 'Department', 'HireDate', 'Salary', 'Email', 'PhoneNumber'])
    return df

# Function to generate random department data
def generate_department_data(num_records):
    data = []
    for i in range(num_records):
        department_id = i + 1
        department_name = fake.job()
        manager_id = fake.random_int(min=100000, max=999999)
        location = fake.city()

        data.append([department_id, department_name, manager_id, location])

    df = pd.DataFrame(data, columns=['DepartmentID', 'DepartmentName', 'ManagerID', 'Location'])
    return df

# Function to generate random customer data
def generate_customer_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        customer_id = fake.unique.random_int(min=100000, max=999999)
        if customer_id not in used_ids:
            used_ids.add(customer_id)
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            address = fake.address().replace("\n", ", ")
            city = fake.city()
            state = fake.state()
            zip_code = fake.zipcode()
            country = fake.country()

            data.append([customer_id, first_name, last_name, email, phone_number, address, city, state, zip_code, country])

    df = pd.DataFrame(data, columns=['CustomerID', 'FirstName', 'LastName', 'Email', 'PhoneNumber', 'Address', 'City', 'State', 'ZipCode', 'Country'])
    return df

# Function to generate random product data
def generate_product_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        product_id = fake.unique.random_int(min=100000, max=999999)
        if product_id not in used_ids:
            used_ids.add(product_id)
            product_name = fake.word()
            category = fake.random_element(elements=('Electronics', 'Clothing', 'Books', 'Toys', 'Home', 'Automotive'))
            price = round(random.uniform(5, 1000), 2)
            stock_quantity = fake.random_int(min=0, max=500)

            data.append([product_id, product_name, category, price, stock_quantity])

    df = pd.DataFrame(data, columns=['ProductID', 'ProductName', 'Category', 'Price', 'StockQuantity'])
    return df

# Function to generate random order data
def generate_order_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        order_id = fake.unique.random_int(min=100000, max=999999)
        if order_id not in used_ids:
            used_ids.add(order_id)
            customer_id = fake.random_int(min=100000, max=999999)
            order_date = fake.date_between(start_date='-5y', end_date='today')
            ship_date = fake.date_between(start_date=order_date, end_date='+30d')
            total_amount = round(random.uniform(20, 2000), 2)
            payment_method = random.choice(['Credit Card', 'PayPal', 'Wire Transfer'])

            data.append([order_id, customer_id, order_date, ship_date, total_amount, payment_method])

    df = pd.DataFrame(data, columns=['OrderID', 'CustomerID', 'OrderDate', 'ShipDate', 'TotalAmount', 'PaymentMethod'])
    return df

# Function to generate random inventory data
def generate_inventory_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        inventory_id = fake.unique.random_int(min=100000, max=999999)
        if inventory_id not in used_ids:
            used_ids.add(inventory_id)
            warehouse_id = fake.random_int(min=1, max=5)
            product_id = fake.random_int(min=100000, max=999999)
            quantity_on_hand = fake.random_int(min=0, max=500)
            last_restocked = fake.date_between(start_date='-2y', end_date='today')

            data.append([inventory_id, warehouse_id, product_id, quantity_on_hand, last_restocked])

    df = pd.DataFrame(data, columns=['InventoryID', 'WarehouseID', 'ProductID', 'QuantityOnHand', 'LastRestocked'])
    return df

# Function to generate random financial transaction data
def generate_transaction_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        transaction_id = fake.unique.random_int(min=100000, max=999999)
        if transaction_id not in used_ids:
            used_ids.add(transaction_id)
            account_id = fake.random_int(min=100000, max=999999)
            transaction_date = fake.date_between(start_date='-5y', end_date='today')
            amount = round(random.uniform(-5000, 5000), 2)
            transaction_type = random.choice(['Debit', 'Credit'])
            description = fake.text(max_nb_chars=50)

            data.append([transaction_id, account_id, transaction_date, amount, transaction_type, description])

    df = pd.DataFrame(data, columns=['TransactionID', 'AccountID', 'TransactionDate', 'Amount', 'TransactionType', 'Description'])
    return df

# Function to generate random marketing campaign data
def generate_campaign_data(num_records):
    data = []
    used_ids = set()
    while len(data) < num_records:
        campaign_id = fake.unique.random_int(min=100000, max=999999)
        if campaign_id not in used_ids:
            used_ids.add(campaign_id)
            campaign_name = fake.catch_phrase()
            start_date = fake.date_between(start_date='-2y', end_date='today')
            end_date = fake.date_between(start_date=start_date, end_date='+6m')
            budget = round(random.uniform(1000, 100000), 2)
            actual_spend = round(random.uniform(1000, budget), 2)

            data.append([campaign_id, campaign_name, start_date, end_date, budget, actual_spend])

    df = pd.DataFrame(data, columns=['CampaignID', 'CampaignName', 'StartDate', 'EndDate', 'Budget', 'ActualSpend'])
    return df

# Generating datasets for each table
employee_df = generate_employee_data(10000)
department_df = generate_department_data(10)
customer_df = generate_customer_data(10000)
product_df = generate_product_data(500)
order_df = generate_order_data(5000)
inventory_df = generate_inventory_data(500)
transaction_df = generate_transaction_data(10000)
campaign_df = generate_campaign_data(1000)

# Saving datasets to CSV files
employee_df.to_csv('employees.csv', index=False)
department_df.to_csv('departments.csv', index=False)
customer_df.to_csv('customers.csv', index=False)
product_df.to_csv('products.csv', index=False)
order_df.to_csv('orders.csv', index=False)
inventory_df.to_csv('inventory.csv', index=False)
transaction_df.to_csv('transactions.csv', index=False)
campaign_df.to_csv('campaigns.csv', index=False)

print("Data generation complete. CSV files saved.")
