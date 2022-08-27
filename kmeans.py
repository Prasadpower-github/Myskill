import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/dsakhinetipa/Videos/Mall_Customers.csv")

x = data.iloc[:, [3, 4]].values  
from sklearn.cluster import KMeans

l =[]

for i in range(1,11):
    Kmeans = KMeans(n_clusters=i, init ='k-means++',random_state = 40)
    Kmeans.fit(x)
    l.append(Kmeans.inertia_)
plt.plot(range(1, 11),l)  
plt.title('The Elobw Method Graph')  
plt.xlabel('Number of clusters(k)')  
plt.ylabel('wcss_list')  
plt.show()  

# =============================================================================
# Kmeans = KMeans(n_clusters=5 ,init ='K-means++', random_state= 42)  
# y_predict = KMeans.fit_predict(x)
# =============================================================================
    