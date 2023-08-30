import pandas as pd

lst = []
fl = open('data_folder\Data\Telangana.txt','r')
for i in fl:
    lst.append(i.strip('\n'))
# print(lst)
fl.close()
# print(len(lst))

df = pd.read_csv('ps3.csv',index_col=0)
cnt = 0
df.set_index("District",inplace=True)
# print(df.head())
for i in range(0,len(lst)):
    df.at[lst[i],'State/UT'] = 'Telangana'
            
df.at['Kargil','State/UT'] = 'Ladakh'
df.at['Leh(Ladakh)','State/UT'] = 'Ladakh'         
            
# print(cnt)

df.reset_index(inplace=True)
# print(df.head())
# print(df[df['State/UT'] == 'Andhra Pradesh'])
# print(df[df['State/UT'] == 'Telangana'])
df.to_csv('ps4.csv')