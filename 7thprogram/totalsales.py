import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Quantity": [5, 10, 8, 3],
    "Price": [50000, 500, 1500, 12000]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Quantity"] * df["Price"]

print(df)
print("Grand Total Sales:", df["Total_Sales"].sum())