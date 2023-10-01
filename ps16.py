import pandas as pd

df = pd.read_csv('ps15.csv',index_col=0)
df = df[['Total_Beds','Population']]
print(df.head(3))
df.to_csv('ps16.csv')
