import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


Y = pd.read_csv("C:/Users/dsakhinetipa/Videos/test.csv")
X = pd.read_csv("C:/Users/dsakhinetipa/Videos/train.csv")

dat = pd.DataFrame({ 'id' :  [1,2, 3,4,5,6,7,8,9,10], 
                     'weather' : ['cloudy', 'monsoon', 'hot','monsoon','cloudy','hot', 'monsoon' ,'cloudy', 'hot', 'cloudy'],
                     'temp'  : [33, 35, 48,33, 32, 52, 40, 28,33,49],
                      'pred ' : [1,0,0,1,0,1,0,1,0,0]})
# =============================================================================
# X_label = X.loc['ram']
# Y_label = X.loc['price_range']
# =============================================================================

plt.figure(figsize=(16,6))

sns.lineplot(data=dat.iloc[1:,1])

