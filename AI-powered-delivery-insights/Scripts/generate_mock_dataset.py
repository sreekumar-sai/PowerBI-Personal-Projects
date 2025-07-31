import pandas as pd
import random
from datetime import datetime, timedelta

# Fixed seed for reproducibility
random.seed(42)

# Parameters
areas = ["Downtown", "Industrial Park", "Suburb North", "Suburb South", "Uptown"]
start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 6, 30)
total_records = 100  # Exactly 100 rows

# Predefined counts based on your dashboard metrics
total_delayed = 20
total_complaints = 16

data = []

# Step 1: Create all records with random areas & dates
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
for _ in range(total_records):
    date = random.choice(dates)
    area = random.choice(areas)
    delay_minutes = 0
    is_delayed = 0
    is_complaint = 0
    data.append([date.date(), area, delay_minutes, is_delayed, is_complaint])

# Step 2: Randomly assign delayed deliveries
delayed_indices = random.sample(range(total_records), total_delayed)
for idx in delayed_indices:
    delay_minutes = round(random.uniform(2, 8), 2)
    data[idx][2] = delay_minutes
    data[idx][3] = 1

# Step 3: Randomly assign complaints from delayed deliveries
complaint_indices = random.sample(delayed_indices, total_complaints)
for idx in complaint_indices:
    data[idx][4] = 1

# Step 4: Create DataFrame & sa
