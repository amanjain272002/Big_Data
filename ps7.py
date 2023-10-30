import pandas as pd
import math
df = pd.read_csv('data_folder\Data\housing.csv')
df = df[['District Name', 'Rural/Urban', 'Total Number of households',
         'Total Number of Livable', 'Total Number of Dilapidated', 'Latrine_premise']]



df2 = pd.read_csv('data_folder\Data\census_2011.csv')

df2 = df2[['District name', 'Households',
           'Rural_Households', 'Urban_Households']]

for i in range(0, len(df2)):
    if (pd.isna(df2.at[i, 'Households'])):
        if (pd.notnull(df2.at[i, 'Rural_Households']) and pd.notnull(df2.at[i, 'Urban_Households'])):
            df2.at[i, 'Households'] = df2.at[i, 'Rural_Households'] + \
                df2.at[i, 'Urban_Households']
        elif (pd.notnull(df2.at[i, 'Urban_Households'])):
            df2.at[i, 'Households'] = df2.at[i, 'Urban_Households']
        else:
            df2.at[i, 'Households'] = df2.at[i, 'Rural_Households']

    if (pd.isna(df2.at[i, 'Rural_Households']) and pd.notnull(df2.at[i, 'Urban_Households'])):
        df2.at[i, 'Rural_Households'] = df2.at[i, 'Households'] - \
            df2.at[i, 'Urban_Households']
    if (pd.isna(df2.at[i, 'Urban_Households']) and pd.notnull(df2.at[i, 'Rural_Households'])):
        df2.at[i, 'Urban_Households'] = df2.at[i, 'Households'] - \
            df2.at[i, 'Rural_Households']


dct = {'District': [], 'Total_Households': [],
       'Households_Rural': [], 'Households_Urban': []}

for i in range(0, len(df2)):
    
    if (df2.loc[i]['District name'] in df.values):
        dct['District'].append(df2.at[i, 'District name'])
        dct['Total_Households'].append(df2.at[i, 'Households'])
        if (pd.notnull(df2.loc[i]['Rural_Households'])):
            dct['Households_Rural'].append(df2.at[i, 'Rural_Households'])

        if (pd.notnull(df2.loc[i]['Urban_Households'])):
            dct['Households_Urban'].append(df2.at[i, 'Urban_Households'])

        if (pd.isna(df2.loc[i]['Rural_Households']) and pd.isna(df2.loc[i]['Urban_Households'])):
            item = df2.at[i, 'Households']
            item = math.ceil(item/2)
            dct['Households_Rural'].append(item)
            dct['Households_Urban'].append(item)
            continue


df3 = pd.DataFrame(dct)
df3['Households_Rural_Livable'] = ""
df3['Households_Urban_Livable'] = ""
df3['Households_Rural_Dilapidated'] = ""
df3['Households_Urban_Dilapidated'] = ""
df3['Households_Rural_Toilet_Premise'] = ""
df3['Households_Urban_Toilet_Premise'] = ""
df3['Households_Total_Livable'] = ""
df3['Households_Total_Dilapidated'] = ""
df3['Households_Total_Toilet_Premise'] = ""

i = 0
j = 0


k = 0
l = 0
m = 0
for i in range(0, len(df)):
    if df.loc[i]['Rural/Urban'] == 'Rural':
        for j in range(k, len(df3)):
            if df.at[i, 'District Name'] == df3.at[j, 'District']:
                df3.at[j, 'Households_Rural_Livable'] = math.ceil(
                    (df.at[i, 'Total Number of Livable']*df3.at[j, 'Households_Rural'])/100)
                df3.at[j, 'Households_Rural_Dilapidated'] = math.ceil(
                    (df.at[i, 'Total Number of Dilapidated']*df3.at[j, 'Households_Rural'])/100)
                df3.at[j, 'Households_Rural_Toilet_Premise'] = math.ceil(
                    (df.at[i, 'Latrine_premise']*df3.at[j, 'Households_Rural'])/100)
                k = j + 1
                break

    elif df.loc[i]['Rural/Urban'] == 'Urban':
        for j in range(l, len(df3)):
            if df.at[i, 'District Name'] == df3.at[j, 'District']:
                df3.at[j, 'Households_Urban_Livable'] = math.ceil(
                    (df.at[i, 'Total Number of Livable']*df3.at[j, 'Households_Urban'])/100)
                df3.at[j, 'Households_Urban_Dilapidated'] = math.ceil(
                    (df.at[i, 'Total Number of Dilapidated']*df3.at[j, 'Households_Urban'])/100)
                df3.at[j, 'Households_Urban_Toilet_Premise'] = math.ceil(
                    (df.at[i, 'Latrine_premise']*df3.at[j, 'Households_Urban'])/100)
                l = j + 1
                break

    elif df.loc[i]['Rural/Urban'] == 'Total':
        for j in range(m, len(df3)):
            if df.at[i, 'District Name'] == df3.at[j, 'District']:
                df3.at[j, 'Households_Total_Livable'] = math.ceil(
                    (df.at[i, 'Total Number of Livable']*df3.at[j, 'Total_Households'])/100)
                df3.at[j, 'Households_Total_Dilapidated'] = math.ceil(
                    (df.at[i, 'Total Number of Dilapidated']*df3.at[j, 'Total_Households'])/100)
                df3.at[j, 'Households_Total_Toilet_Premise'] = math.ceil(
                    (df.at[i, 'Latrine_premise']*df3.at[j, 'Total_Households'])/100)
                m = j + 1
                break

for i in range(0, len(df3)):
    if (pd.isna(df3.at[i, 'Households_Rural_Livable']) and pd.notull(df3.at[i, 'Households_Urban_Livable'])):
        if (df3.at[j, 'Households_Total_Livable'] - df3.at[i, 'Households_Urban_Livable'] > 0):
            df3.at[i, 'Households_Rural_Livable'] = df3.at[j,
                                                           'Households_Total_Livable'] - df3.at[i, 'Households_Urban_Livable']

    if (pd.isna(df3.at[i, 'Households_Urban_Livable']) and pd.notnull(df3.at[i, 'Households_Rural_Livable'])):
        if (df3.at[j, 'Households_Total_Livable'] - df3.at[i, 'Households_Rural_Livable'] > 0):
            df3.at[i, 'Households_Urban_Livable'] = df3.at[j,
                                                           'Households_Total_Livable'] - df3.at[i, 'Households_Rural_Livable']

    if (pd.isna(df3.at[i, 'Households_Rural_Dilapidated']) and pd.notnull(df3.at[i, 'Households_Urban_Dilapidated'])):
        if (df3.at[j, 'Households_Total_Dilapidated'] - df3.at[i, 'Households_Urban_Dilapidated'] > 0):
            df3.at[i, 'Households_Rural_Dilapidated'] = df3.at[j,
                                                               'Households_Total_Dilapidated'] - df3.at[i, 'Households_Urban_Dilapidated']

    if (pd.isna(df3.at[i, 'Households_Urban_Dilapidated']) and pd.notnull(df3.at[i, 'Households_Rural_Dilapidated'])):
        if (df3.at[j, 'Households_Total_Dilapidated'] - df3.at[i, 'Households_Rural_Dilapidated'] > 0):
            df3.at[i, 'Households_Urban_Dilapidated'] = df3.at[j,
                                                               'Households_Total_Dilapidated'] - df3.at[i, 'Households_Rural_Dilapidated']

    if (pd.isna(df3.at[i, 'Households_Rural_Toilet_Premise']) and pd.notnull(df3.at[i, 'Households_Urban_Toilet_Premise'])):
        if (df3.at[j, 'Households_Total_Toilet_Premise'] - df3.at[i, 'Households_Urban_Toilet_Premise'] > 0):
            df3.at[i, 'Households_Rural_Toilet_Premise'] = df3.at[j,
                                                                  'Households_Total_Toilet_Premise'] - df3.at[i, 'Households_Urban_Toilet_Premise']

    if (pd.isna(df3.at[i, 'Households_Urban_Toilet_Premise']) and pd.notnull(df3.at[i, 'Households_Rural_Toilet_Premise'])):
        if (df3.at[j, 'Households_Total_Toilet_Premise'] - df3.at[i, 'Households_Rural_Toilet_Premise'] > 0):
            df3.at[i, 'Households_Urban_Toilet_Premise'] = df3.at[j,
                                                                  'Households_Total_Toilet_Premise'] - df3.at[i, 'Households_Rural_Toilet_Premise']


# df3.to_csv('df3.csv')
# df2.to_csv('df2.csv')

house = df3[['District', 'Households_Rural', 'Households_Rural_Livable', 'Households_Rural_Dilapidated', 'Households_Rural_Toilet_Premise',
             'Households_Urban', 'Households_Urban_Livable', 'Households_Urban_Dilapidated', 'Households_Urban_Toilet_Premise']]

# house.to_csv('ps7.csv')
house.to_csv('clean_data\housing.csv')