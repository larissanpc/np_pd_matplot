import numpy as np
import pandas as pd
#Consider the following Python dictionary data and Python list labels: 
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'], 
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3], 
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
#Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data,labels)
df
df = pd.DataFrame(data,index=labels) #Create a DataFrame df from this dictionary data which has the index labels.
df
df.loc[df.isnull().any(axis=1)]
