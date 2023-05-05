import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data,index=labels) #Create a DataFrame df from this dictionary data which has the index labels.
df.describe #1) Display a summary of the basic information about this DataFrame and its data.

df.head(3) #2) Return the first 3 rows of the DataFrame df.

data_df = pd.DataFrame(data, index=labels)
data2= data_df.loc[['c','d','h'],['animal','age']]
print(data2)

#4) Select the rows where the age is missing. 
df.loc[df.isnull().any(axis=1)]

#5) Select the rows where the animal is a cat and the age is less than 3
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
result = df[(df.animal == 'cat') & (df.age < 3)]
print(result)

#6) Change the age in row 'f' to 1.5
df.loc['f', 'age'] = 1.5
print(df)

#7) Calculate the mean age for each different animal in df
print(df['age'].mean())
