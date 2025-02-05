import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("assignmentOne_PythonRefresher/fibTimeLog.csv")
df = pd.DataFrame(data)
print(df)

plt.plot(df["input"], df["executionTime"])
plt.title("Execution Time of fib(100): With Cache")
plt.xlabel("Fib(n)")
plt.ylabel("Execution Time (s)")
plt.show()
