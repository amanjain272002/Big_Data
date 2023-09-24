import pandas as pd;

df1 = pd.read_csv('ps8.csv',index_col=0)
df1 = df1[['State','Population']]


df2 = pd.read_csv('ps11.csv',index_col=0)
df2 = df2[['State/UT','HospitalBeds']]

df2['Population'] = 0
lsthos = []
for i in range(0,len(df2)):
    for j in range(0,len(df1)):
        if(df1.at[j,'State'] == df2.at[i,'State/UT']):
            df2.at[i,'Population'] = df1.at[j,'Population']
        

df3 = pd.read_csv('ps4.csv',index_col=0)
df3  = df3[['State/UT','Population']]
totalpop = 0
totalbeds = 0
for i in range(0,len(df2)):
    sum = 0
    for j in range(0,len(df3)):
        s = df3.at[j,'State/UT']
        s = s.upper()
        if(df2.at[i,'Population'] == 0 and df2.at[i,'State/UT'] == s):
            sum = sum + df3.at[j,'Population']
    
    if(df2.at[i,'Population'] == 0):
        df2.at[i,'Population'] = sum
    totalbeds = totalbeds + df2.at[i,'HospitalBeds']
    totalpop  = totalpop + df2.at[i,'Population']

df2.at[36,'State/UT'] = 'National'
df2.at[36,'Population'] = totalpop
df2.at[36,'HospitalBeds'] = totalbeds
df2.to_csv('ps12.csv')