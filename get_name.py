import os
from openpyxl import Workbook
import numpy as np
#import json
import pandas as pd
import random

file_path="/home/nwang/emotion/dataset/DEMOS/"

names=os.listdir(file_path)

datalist = []
maleset =[]
famaleset=[]
#print(names)
#print(type(names))
for name in names:
    _, sex, id, emo = name.split('_')
    datalist.append({"id":id, "sex":sex,"emo":emo[:3], "filename":name})
    #print("sex:{}, id:{}, emo:{}".format(sex,id,emo[:3]))

print("finish,data size is {}".format(len(datalist)))

for data in datalist:
    if data['sex'] == 'f':
        famaleset.append(data)
    else:
        maleset.append(data)

#print("male: {}, famale:{}".format(len(maleset),len(famaleset)))

#选独特男id,只留下唯一的id，缺少35号
mdata = pd.DataFrame(maleset).set_index('id',drop=False)
# diffm = mdata.drop_duplicates(subset=['id'], keep='first',inplace=False)
# print(diffm)
# print("length of data: {}".format(len(diffm)))

mid_list = mdata['id'].unique()  #提取独一无二id
random.shuffle(mid_list) ##打乱id顺序
len_mid = len(mid_list)
index=[round(len_mid*0.4),round(len_mid*0.7)]

m_train_id_set = mid_list[:index[0]]
m_test_id_set = mid_list[index[0]:index[1]]
m_dev_id_set = mid_list[index[1]:]

df_m_train = mdata.loc[m_train_id_set].copy(deep=True)
df_m_test = mdata.loc[m_test_id_set].copy(deep=True)
df_m_dev = mdata.loc[m_dev_id_set].copy(deep=True)

#女id处理
fdata = pd.DataFrame(famaleset).set_index('id',drop=False)
fid_list = fdata['id'].unique()  #提取独一无二id
random.shuffle(fid_list) ##打乱id顺序
len_fid = len(fid_list)
index=[round(len_fid*0.4),round(len_fid*0.7)]

f_train_id_set = fid_list[:index[0]]
f_test_id_set = fid_list[index[0]:index[1]]
f_dev_id_set = fid_list[index[1]:]

df_f_train = fdata.loc[f_train_id_set].copy(deep=True)
df_f_test = fdata.loc[f_test_id_set].copy(deep=True)
df_f_dev = fdata.loc[f_dev_id_set].copy(deep=True)

df_train =  pd.concat([df_m_train,df_f_train],axis=0)
df_test =  pd.concat([df_m_test,df_f_test],axis=0)
df_dev =  pd.concat([df_m_dev,df_f_dev],axis=0)

#统计emo数目 
a1=df_f_train.loc[df_f_train['emo']=='col'].shape[0]
b1=df_m_train.loc[df_m_train['emo']=='col'].shape[0]
c1=df_f_test.loc[df_f_test['emo']=='col'].shape[0]
d1=df_m_test.loc[df_m_test['emo']=='col'].shape[0]
e1=df_f_dev.loc[df_f_dev['emo']=='col'].shape[0]
f1=df_m_dev.loc[df_m_dev['emo']=='col'].shape[0]
print('col',a1,b1,c1,d1,e1,f1)
g1=df_train.loc[df_train['emo']=='col'].shape[0]
h1=df_test.loc[df_test['emo']=='col'].shape[0]
i1=df_dev.loc[df_dev['emo']=='col'].shape[0]
print('col',g1,i1,h1)


a2=df_f_train.loc[df_f_train['emo']=='dis'].shape[0]
b2=df_m_train.loc[df_m_train['emo']=='dis'].shape[0]
c2=df_f_test.loc[df_f_test['emo']=='dis'].shape[0]
d2=df_m_test.loc[df_m_test['emo']=='dis'].shape[0]
e2=df_f_dev.loc[df_f_dev['emo']=='dis'].shape[0]
f2=df_m_dev.loc[df_m_dev['emo']=='dis'].shape[0]
print('dis',a2,b2,c2,d2,e2,f2)
g2=df_train.loc[df_train['emo']=='dis'].shape[0]
h2=df_test.loc[df_test['emo']=='dis'].shape[0]
i2=df_dev.loc[df_dev['emo']=='dis'].shape[0]
print('dis',g2,i2,h2)

a3=df_f_train.loc[df_f_train['emo']=='gio'].shape[0]
b3=df_m_train.loc[df_m_train['emo']=='gio'].shape[0]
c3=df_f_test.loc[df_f_test['emo']=='gio'].shape[0]
d3=df_m_test.loc[df_m_test['emo']=='gio'].shape[0]
e3=df_f_dev.loc[df_f_dev['emo']=='gio'].shape[0]
f3=df_m_dev.loc[df_m_dev['emo']=='gio'].shape[0]
print('gio',a3,b3,c3,d3,e3,f3)
g3=df_train.loc[df_train['emo']=='gio'].shape[0]
h3=df_test.loc[df_test['emo']=='gio'].shape[0]
i3=df_dev.loc[df_dev['emo']=='gio'].shape[0]
print('gio',g3,i3,h3)

a4=df_f_train.loc[df_f_train['emo']=='pau'].shape[0]
b4=df_m_train.loc[df_m_train['emo']=='pau'].shape[0]
c4=df_f_test.loc[df_f_test['emo']=='pau'].shape[0]
d4=df_m_test.loc[df_m_test['emo']=='pau'].shape[0]
e4=df_f_dev.loc[df_f_dev['emo']=='pau'].shape[0]
f4=df_m_dev.loc[df_m_dev['emo']=='pau'].shape[0]
print('pau',a4,b4,c4,d4,e4,f4)
g4=df_train.loc[df_train['emo']=='pau'].shape[0]
h4=df_test.loc[df_test['emo']=='pau'].shape[0]
i4=df_dev.loc[df_dev['emo']=='pau'].shape[0]
print('pau',g4,i4,h4)

a5=df_f_train.loc[df_f_train['emo']=='rab'].shape[0]
b5=df_m_train.loc[df_m_train['emo']=='rab'].shape[0]
c5=df_f_test.loc[df_f_test['emo']=='rab'].shape[0]
d5=df_m_test.loc[df_m_test['emo']=='rab'].shape[0]
e5=df_f_dev.loc[df_f_dev['emo']=='rab'].shape[0]
f5=df_m_dev.loc[df_m_dev['emo']=='rab'].shape[0]
print('rab',a5,b5,c5,d5,e5,f5)
g5=df_train.loc[df_train['emo']=='rab'].shape[0]
h5=df_test.loc[df_test['emo']=='rab'].shape[0]
i5=df_dev.loc[df_dev['emo']=='rab'].shape[0]
print('rab',g5,i5,h5)

a6=df_f_train.loc[df_f_train['emo']=='sor'].shape[0]
b6=df_m_train.loc[df_m_train['emo']=='sor'].shape[0]
c6=df_f_test.loc[df_f_test['emo']=='sor'].shape[0]
d6=df_m_test.loc[df_m_test['emo']=='sor'].shape[0]
e6=df_f_dev.loc[df_f_dev['emo']=='sor'].shape[0]
f6=df_m_dev.loc[df_m_dev['emo']=='sor'].shape[0]
print('sor',a6,b6,c6,d6,e6,f6)
g6=df_train.loc[df_train['emo']=='sor'].shape[0]
h6=df_test.loc[df_test['emo']=='sor'].shape[0]
i6=df_dev.loc[df_dev['emo']=='sor'].shape[0]
print('sor',g6,i6,h6)

a7=df_f_train.loc[df_f_train['emo']=='tri'].shape[0]
b7=df_m_train.loc[df_m_train['emo']=='tri'].shape[0]
c7=df_f_test.loc[df_f_test['emo']=='tri'].shape[0]
d7=df_m_test.loc[df_m_test['emo']=='tri'].shape[0]
e7=df_f_dev.loc[df_f_dev['emo']=='tri'].shape[0]
f7=df_m_dev.loc[df_m_dev['emo']=='tri'].shape[0]
print('tri',a7,b7,c7,d7,e7,f7)
g7=df_train.loc[df_train['emo']=='tri'].shape[0]
h7=df_test.loc[df_test['emo']=='tri'].shape[0]
i7=df_dev.loc[df_dev['emo']=='tri'].shape[0]
print('tri',g7,i7,h7)



df_train.to_csv("train_dataset.csv",index=False)
df_test.to_csv("test_dataset.csv",index=False)
df_dev.to_csv("dev_dataset.csv",index=False)
