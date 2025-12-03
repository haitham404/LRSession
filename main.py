import pandas as pd
import numpy as np

# 1️⃣ نكبر عدد الشقق
num_apartments = 50  # نعمل 50 شقة كمثال

np.random.seed(0)  # للتكرار

data = {
    "Apartment_ID": list(range(1, num_apartments+1)),
    "Size_m2": np.random.randint(50, 200, size=num_apartments),        # مساحات بين 50 و 200 م2
    "Rooms": np.random.randint(1, 5, size=num_apartments),             # عدد الغرف بين 1 و 4
    "Floor": np.random.randint(1, 15, size=num_apartments),            # الطابق بين 1 و 15
    "Location_Score": np.round(np.random.uniform(5, 10, size=num_apartments), 1),  # تقييم الموقع بين 5 و 10
}

df = pd.DataFrame(data)

# 2️⃣ نعمل Price خطي من الأعمدة الأخرى
# Price = 1000*Size + 20000*Rooms + 5000*Floor + 10000*Location_Score + small noise
noise = np.random.randint(-5000, 5000, size=num_apartments)
df['Price_USD'] = 1000*df['Size_m2'] + 20000*df['Rooms'] + 5000*df['Floor'] + 10000*df['Location_Score'] + noise

# 3️⃣ حفظ CSV
df.to_csv("apartments_table_linear.csv", index=False)

print("CSV file with 50 apartments (linear prices) created successfully!")
print(df.head(10))  # عرض أول 10 شقق
