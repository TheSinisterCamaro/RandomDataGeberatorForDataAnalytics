import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate random budget data
def generate_budget_data(num_records):
    data = []
    for _ in range(num_records):
        budget_id = fake.unique.random_int(min=100000, max=999999)
        department_id = fake.random_int(min=1, max=10)  # Assuming 10 departments
        fiscal_year = fake.random_int(min=2018, max=2024)
        budget_amount = round(random.uniform(10000, 1000000), 2)
        actual_amount = round(random.uniform(5000, budget_amount), 2)
        
        data.append([budget_id, department_id, fiscal_year, budget_amount, actual_amount])
    
    df = pd.DataFrame(data, columns=['BudgetID', 'DepartmentID', 'FiscalYear', 'BudgetAmount', 'ActualAmount'])
    return df

# Function to generate random account data
def generate_account_data(num_records):
    data = []
    for _ in range(num_records):
        account_id = fake.unique.random_int(min=100000, max=999999)
        account_name = fake.company_suffix()
        account_type = random.choice(['Checking', 'Savings', 'Credit'])
        opening_balance = round(random.uniform(1000, 50000), 2)
        current_balance = round(random.uniform(0, opening_balance), 2)
        
        data.append([account_id, account_name, account_type, opening_balance, current_balance])
    
    df = pd.DataFrame(data, columns=['AccountID', 'AccountName', 'AccountType', 'OpeningBalance', 'CurrentBalance'])
    return df

# Generating datasets for Budgets and Accounts tables
budget_df = generate_budget_data(100)
account_df = generate_account_data(100)

# Saving datasets to CSV files
budget_df.to_csv('budgets.csv', index=False)
account_df.to_csv('accounts.csv', index=False)

print("Data generation complete. CSV files for Budgets and Accounts saved.")

