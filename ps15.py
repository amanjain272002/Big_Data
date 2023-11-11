import pandas as pd

df = pd.read_csv('ps14.csv',index_col=0)
df1 = pd.read_csv('ps12.csv',index_col=0)
df['Total_Beds'] = df['Rural_Government_Beds'] + df['Urban_Government_Beds']
df['Total_Hospitals'] = df['Rural_Government_Hospitals'] + df['Urban_Government_Hospitals']
# print(df.columns)
df1.drop(df1.tail(1).index,inplace=True)
df.set_index(keys='State/UT',inplace=True)

df['Population'] = 0
for i in range(0,len(df1)):
    str1 = df1.at[i,'State/UT']
    if (str1 in df.index) :
        df.at[str1,'Total_Beds'] = df.at[str1,'Total_Beds'] + df1.at[i,'HospitalBeds']
        df.at[str1,'Population'] = df1.at[i,'Population']

df.to_csv('ps15.csv')
df.to_csv('government_hospital.csv')
