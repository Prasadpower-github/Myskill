



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 

data = pd.read_csv("C:/Users/dsakhinetipa/Videos/python files/CarPrice_Assignment.csv")

data.plot(x='CarName', y= 'price', color ="g")  
plt.title('region')  
plt.xlabel('CarName')  
plt.ylabel('price')  
plt.show()



X = data['wheelbase'].values.reshape(-1,1)
y =  data['price'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=1)

regressor = LinearRegression()
regressor.fit(X_test, y_test)

y_pred = regressor.predict(y_test)

print(int(y_pred)%100)





