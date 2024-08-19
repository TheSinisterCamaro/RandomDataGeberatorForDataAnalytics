import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate random lead data
def generate_lead_data(num_records):
    data = []
    for _ in range(num_records):
        lead_id = fake.unique.random_int(min=100000, max=999999)
        campaign_id = fake.random_int(min=100000, max=999999)
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        lead_source = random.choice(['Website', 'Social Media', 'Referral', 'Email Campaign', 'Direct Mail'])
        status = random.choice(['New', 'Contacted', 'Qualified', 'Converted', 'Closed'])
        
        data.append([lead_id, campaign_id, first_name, last_name, email, phone_number, lead_source, status])
    
    df = pd.DataFrame(data, columns=['LeadID', 'CampaignID', 'FirstName', 'LastName', 'Email', 'PhoneNumber', 'LeadSource', 'Status'])
    return df

# Function to generate random promotion data
def generate_promotion_data(num_records):
    data = []
    for _ in range(num_records):
        promotion_id = fake.unique.random_int(min=100000, max=999999)
        promotion_name = fake.catch_phrase()
        start_date = fake.date_between(start_date='-2y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+6m')
        discount_percentage = round(random.uniform(5, 50), 2)
        product_id = fake.random_int(min=100000, max=999999)
        
        data.append([promotion_id, promotion_name, start_date, end_date, discount_percentage, product_id])
    
    df = pd.DataFrame(data, columns=['PromotionID', 'PromotionName', 'StartDate', 'EndDate', 'DiscountPercentage', 'ProductID'])
    return df

# Generating datasets for Leads and Promotions tables
lead_df = generate_lead_data(100)
promotion_df = generate_promotion_data(100)

# Saving datasets to CSV files
lead_df.to_csv('leads.csv', index=False)
promotion_df.to_csv('promotions.csv', index=False)

print("Data generation complete. CSV files for Leads and Promotions saved.")

