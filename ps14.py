import pandas as pd
from datetime import datetime
df = pd.read_csv('ps13.csv',index_col=0)
def ps(s):
    if '*' in s:
        s = s.replace('*','')
        return s.upper()
    if '&' in s:
        s = s.replace('&','and')
        return s.upper()
    elif 'Delhi' in s:
        s = s.replace('Delhi','NCT OF DELHI')
        return s.upper()
    elif 'Odisha' in s:
        s = s.replace('Odisha','ORISSA')
        return s.upper()
    elif 'Puducherry' in s:
        s = s.replace('Puducherry','PONDICHERRY')
        return s.upper()
    else:
        return s.upper()


df['Last_Updated']=pd.to_datetime(df['Last_Updated'],format = '%d.%m.%Y')

for i in range(0,len(df)):
    df.at[i,'State/UT'] = ps(df.at[i,'State/UT'])

df.to_csv('ps14.csv')

