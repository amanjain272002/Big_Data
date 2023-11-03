import pandas as pd

df = pd.read_csv('ps5.csv',index_col=0)
df.to_csv('clean_data/census.csv')