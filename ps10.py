import pandas as pd

df = pd.read_csv('data_folder\Data\hospitals.csv')
df1 = pd.read_csv('data_folder\Data\metadata.csv')

# print(df.columns)
# print(df1)
lst = []
for i in range(0,len(df1)):
    
    ele = df1.loc[i]['Acronyms']
    ele = ele.replace(',','')
    lst.append(ele)

df.rename(columns={'Unnamed: 0':'State/UT','PHC':lst[0],'CHC':lst[1],'SDH':lst[2],'DH':lst[3]},inplace=True)
# print(df.columns)
df.to_csv('ps10.csv')