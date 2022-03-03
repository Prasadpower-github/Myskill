
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/dsakhinetipa/Downloads/inventory-berlin.csv")

df = pd.DataFrame(data)
  
X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])

plt.bar(X, Y, color='r')
plt.title("berlin items")
plt.xlabel("count")
plt.ylabel("item")
  

plt.show()
