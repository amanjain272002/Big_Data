import pandas as pd

df = pd.read_csv('ps10.csv',index_col=0)

def ps(s):
    return s.upper()

for i in range(0,len(df)):
    df.at[i,'State/UT'] = ps(df.at[i,'State/UT'])

df.drop(df.tail(1).index,inplace=True)
df.to_csv('ps11.csv')