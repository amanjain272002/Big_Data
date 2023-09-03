import pandas as pd

df = pd.read_csv('ps5.csv')
df.to_csv('clean_data/census.csv')