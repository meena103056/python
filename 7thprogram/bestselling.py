import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Sales": [250000, 5000, 12000, 36000]
}

df = pd.DataFrame(data)

best = df.loc[df["Sales"].idxmax()]

print("Best Selling Product")
print(best)