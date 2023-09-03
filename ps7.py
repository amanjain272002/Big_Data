import pandas as pd

df = pd.read_csv('data_folder\Data\housing.csv')
df = df[['District Name','Rural/Urban','Total Number of households','Total Number of Livable','Total Number of Dilapidated','Latrine_premise']]

df2 = pd.read_csv('ps5.csv')
df2 = df2[['District','Households']]



