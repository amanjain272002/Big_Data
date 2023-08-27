import pandas as pd
df = pd.read_csv('ps1.csv',index_col=0)

df = df.rename(columns={'State name':'State/UT','District name':'District','Male_Literate':'Literate_Male','Female_Literate':'Literate_Female',
                   'Rural_Households':'Households_Rural','Urban_ Households':'Households_Urban','Age_Group_0_29':'Young_and_Adult',
                   'Age_Group_30_49':'Middle_Aged','Age_Group_50':'Senior_Citizen','Age not stated':'Age_Not_Stated'})
# print(df.head(4))
# print(df)
df.to_csv('ps2.csv')
