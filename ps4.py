import pandas as pd

lst = []
fl = open('data_folder\Data\Telangana.txt','r')
for i in fl:
    lst.append(i.strip('\n'))
print(lst)
fl.close()
print(len(lst))

df = pd.read_csv('ps3.csv',index_col=0)
cnt = 0
for st in range(0,len(df['State/UT'])):
    if ((df.loc[st]['State/UT'] == 'Andhra Pradesh') and (df.loc[st]['District'] in lst)):
        df.replace(df.loc[st]['State/UT'] , 'Telangana')
            
         
            
# print(cnt)
# print(df[df['State/UT'] == 'Andhra Pradesh'])
print(df[df['State/UT'] == 'Telangana'])