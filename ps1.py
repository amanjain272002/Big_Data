import pandas as pd

df = pd.read_csv('data_folder/Data/census_2011.csv')
df = df[['State name','District name','Population','Male','Female','Literate','Male_Literate','Female_Literate','Rural_Households',
          'Urban_Households','Households','Age_Group_0_29','Age_Group_30_49','Age_Group_50','Age not stated']]
# print(df)
df.to_csv('ps1.csv')


 