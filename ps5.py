import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ps4.csv',index_col=0)

l = len(df.index)
dct = {}
dct2 = {}
lst1 = []
lst2 = []
lst3 = []

for i in df.columns:
    lst4 = []
    if pd.isnull(df[i]).any().sum()!=0:
        lst4.append(df[i].isnull().sum())
        dct2[i] = lst4
        lst1.append(i)
        lst2.append((df[i].isnull().sum()/l)*100)

for j in df.columns:
    if pd.isnull(df[j]).any().sum()!=0:
        for i in range(0,l):
            if j == 'Population' and pd.isna(df.loc[i][j]) and pd.notnull(df.loc[i]['Male']) and pd.notnull(df.loc[i]['Female']):
                df.at[i,j] = df.at[i,'Male'] + df.at[i,'Female']

            elif j == 'Literate' and pd.isna(df.loc[i][j]) and pd.notnull(df.loc[i]['Literate_Male']) and pd.notnull(df.loc[i]['Literate_Female']):
                df.at[i,j] = df.at[i,'Literate_Male'] + df.at[i,'Literate_Female']

            elif j == 'Households' and pd.isna(df.loc[i][j]) and pd.notnull(df.loc[i]['Households_Rural']) and pd.notnull(df.loc[i]['Urban_Households']):
                df.at[i,j] =df.at[i,'Households_Rural'] + df.at[i,'Urban_Households']

for i in df.columns:
    if pd.isnull(df[i]).any().sum()!=0:
        lst3.append((df[i].isnull().sum()/l)*100)


dct['x'] = lst1
dct['Old_data'] = lst2
dct['Updated_data'] = lst3
if(len(lst1) == len(lst2) and len(lst2) == len(lst3)):
    print(dct)
# print(lst3)
print("Printing total number of missing cells in each column => ")
print(dct2)    

df.to_csv('ps5.csv')
df1 = pd.DataFrame(dct)
df1.set_index('x',inplace=True)
df1.plot(kind='bar',title='Find and process Missing Data')
plt.show()
