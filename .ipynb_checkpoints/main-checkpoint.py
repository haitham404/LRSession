import pandas as pd

# Create sample apartment table
data = {
    "Apartment_ID": [1, 2, 3, 4, 5],
    "Size_m2": [80, 120, 95, 150, 60],
    "Rooms": [2, 3, 2, 4, 1],
    "Floor": [3, 5, 2, 10, 1],
    "Location_Score": [7.8, 8.5, 6.9, 9.1, 5.5],
    "Price_USD": [90000, 150000, 110000, 220000, 70000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("apartments_table.csv", index=False)

print("CSV file created successfully!")
