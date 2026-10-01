import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [50000, 500, 1500]
}

df = pd.DataFrame(data)

df["Discount_Price"] = df["Price"] * 0.90

print(df)