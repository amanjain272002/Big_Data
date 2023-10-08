import pandas as pd

# df = pd.read_csv('ps15.csv',index_col=0)
# df = df[['Total_Beds','Population','Total_Hospitals']]

# df.to_csv('ps17.csv')
df = pd.read_csv('ps14.csv',index_col=0)
df.set_index('State/UT',inplace=True)
df.to_csv('ps17.csv')