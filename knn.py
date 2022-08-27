import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({ 'id' :  [1,2, 3,4,5,6,7,8,9,10], 
                     'weather' : ['cloudy', 'monsoon', 'hot','monsoon','cloudy','hot', 'monsoon' ,'cloudy', 'hot', 'cloudy'],
                     'temp'  : [33, 35, 48,33, 32, 52, 40, 28,33,49],
                      'pred ' : [1,0,0,1,0,1,0,1,0,1]})

X = data.loc[:,[ 'id', 'temp']]
Y = data.iloc[:, 3]

print(X)
print(Y)



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(y_pred)



