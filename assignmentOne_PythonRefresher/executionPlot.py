import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("fibTimeLog.csv")
df = pd.DataFrame(data)
print(df)

plt.plot(df["input"], df["executionTime"])
plt.show()
