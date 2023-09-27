import pandas as pd

df = pd.read_csv('data_folder\Data\government_hospitals.csv',index_col=0)
df.dropna(how='any',inplace=True)
df.reset_index(inplace=True)
df.rename(columns={'States/UTs':'State/UT','Rural hospitals':'Rural_Government_Hospitals','Unnamed: 2':'Rural_Government_Beds','Urban hospitals':'Urban_Government_Hospitals','Unnamed: 4':'Urban_Government_Beds','As on':'Last_Updated'},inplace=True)
df.to_csv('ps13.csv')