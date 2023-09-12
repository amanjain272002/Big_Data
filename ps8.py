import pandas as pd

df = pd.read_csv('data_folder\Data\census_2011.csv')

df = df[['State name','District name','Having_latrine_facility_within_the_premises_Total_Households','Population','Male','Female']]
# print(df.count('index'))
# print(df.head(5))
for i in range(0,len(df)):
    if pd.isna(df.at[i,'Population']):
        df.at[i,'Population'] = df.at[i,'Male'] + df.at[i,'Female']

df1 = pd.read_csv('ps7.csv')
df1 = df1[['District','Households_Rural','Households_Urban']]
# print(df1.count('index'))
tothouse = []
for i in range(0,len(df1)):
    tothouse.append(df1.at[i,'Households_Rural'] + df1.at[i,'Households_Urban'])

df1['Total_HouseHolds'] = tothouse

k = 0
state = []
latrine = []
population = []
for i in range(0,len(df1)):
    for j in range(k,len(df)):
        if (df1.loc[i]['District'] == df.loc[j]['District name']):
            state.append(df.at[j,'State name'])
            latrine.append(df.at[j,'Having_latrine_facility_within_the_premises_Total_Households'])
            population.append(df.at[j,'Population'])
            k = j + 1
            break

df1['State'] = state
df1['Toilet'] = latrine
df1['Population'] = population

# print(len(df1['Toilet']))

# df1.dropna(axis=0,how='any',inplace=True)
df1.set_index(keys='State',inplace=True)
# print(len(df1))

State = set(state)
# print(df1)
ps = {'State' : [],'Toilet':[],'Total Household':[],'Urban':[],'Rural':[],'Population':[]}
for i in State:
    ps['State'].append(i)
    ps['Toilet'].append(df1.loc[i]['Toilet'].sum())
    ps['Total Household'].append(df1.loc[i]['Total_HouseHolds'].sum())
    ps['Urban'].append(df1.loc[i]['Households_Urban'].sum())
    ps['Rural'].append(df1.loc[i]['Households_Rural'].sum())
    ps['Population'].append(df1.loc[i]['Population'].sum())

ps = pd.DataFrame(ps)
ps.to_csv('ps8.csv')