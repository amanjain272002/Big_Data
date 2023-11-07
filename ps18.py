import pandas as pd

# df = pd.read_csv('clean_data/census.csv',index_col=0)
# df.set_index('District',inplace=True)
# print(df.head(3))
# df.to_csv('census.csv')

# df = pd.read_csv('clean_data/housing.csv',index_col=0)
# df.set_index('District',inplace=True)
# print(df.head(3))
# df.to_csv('housing.csv')

# df = pd.read_csv('clean_data/all_hospitals.csv',index_col=0)
# df.set_index('State/UT',inplace=True)
# print(df.head(3))
# df.to_csv('all_hospitals.csv')

df1 = pd.read_csv('housing.csv',index_col=0)
# print(df1.head(3))
df1.reset_index(inplace=True)

df2 = pd.read_csv('census.csv',index_col=0)

df2.reset_index(inplace=True)
# print(df2.head(3))

lst_State = []
for i in range(0,len(df1)):
    for j in range(i,len(df2)):
        if df1.at[i,'District'] == df2.at[j,'District']:
            lst_State.append(df2.at[j,'State/UT'])
            break

# print(df2.at['Hamirpur','State/UT'])

# print(lst_State)
# print(len(lst_State))
df1['State_UT'] = lst_State
# print(df1.head(3))
df1.set_index('District',inplace=True)
df1.to_csv('housing1.csv')