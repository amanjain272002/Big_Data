import pandas as pd

df = pd.read_csv('ps10.csv',index_col=0)

def ps(s):
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
    

for i in range(0,len(df)):
    df.at[i,'State/UT'] = ps(df.at[i,'State/UT'])

df.drop(df.tail(1).index,inplace=True)
df.to_csv('ps11.csv')