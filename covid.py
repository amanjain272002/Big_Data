import pandas as pd

df = pd.read_csv('PowerbiProject.csv')

df = df[['country','indicator','date','value']]
print(df.head(5))
df.to_csv('covid.csv')
