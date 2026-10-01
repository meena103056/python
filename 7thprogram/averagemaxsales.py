import pandas as pd
import numpy as np

sales = [2500, 4000, 3500, 6000, 4500]

arr = np.array(sales)

print("Average Sales:", np.mean(arr))
print("Maximum Sales:", np.max(arr))
print("Minimum Sales:", np.min(arr))