import pandas as pd

df = pd.read_csv('ps2.csv',index_col=0)

for i in range(0,len(df['State/UT'])):
    str = df.loc[i]['State/UT']
    str = str.lower()
    lst = list(str)
    for j in range(0,len(lst)):
        if j == 0:
            s = lst[0]
            s = s.upper()
            lst[j] =  s
        elif lst[j] == ' ' and lst[j+1]!='a' and lst[j+2]!='n' and lst[j+3]!='d':
            s = lst[j+1]
            s = s.upper()
            lst[j+1] = s
    str = ''.join(lst)
    df.replace(df.loc[i]['State/UT'],str,inplace=True)

df.to_csv('ps3.csv')