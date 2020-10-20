import pandas as pd
import numpy as np
import os
import re
from datetime import datetime


final_file=pd.read_csv("final_file.csv").drop(['Unnamed: 0'],axis=1)
scripts_file=pd.DataFrame(columns=['stockname','ema5','ema10','ema30','ema60'])
print(scripts_file)


def ema(index_of_stock,index_of_date,emano):
    emano=emano[emano.find("ema")+3:]
    if(index_of_date>=2+int(emano)):
        pre_ema1=((final_file.iloc[index_of_stock,2+int(emano)]-(np.mean(final_file.iloc[index_of_stock,2:2+int(emano)])))*(2/(int(emano)+1)))+np.mean(final_file.iloc[index_of_stock,2:2+int(emano)])
        
    if(index_of_date>2+int(emano)):
        for x in range(8,index_of_date):
            ema1=((final_file.iloc[index_of_stock,x]-pre_ema1)*(2/(int(emano)+1)))+pre_ema1
            pre_ema1=ema1
    return pre_ema1 

stock_names=(final_file['SYMBOL'])

for stock in stock_names:
    y=(final_file.columns)
    ema_date=(y[len(y)-1])
    index_date=final_file.columns.get_loc(ema_date)
    index_stock=int(final_file[final_file['SYMBOL']==stock].index.values)
    scripts_file=scripts_file.append(pd.Series([stock,ema(index_stock,index_date,"ema5"),ema(index_stock,index_date,"ema10"),ema(index_stock,index_date,"ema30"),ema(index_stock,index_date,"ema60")],index=['stockname','ema5','ema10','ema30','ema60']),ignore_index=True)

    
print(scripts_file)
scripts_file.to_csv('ema_file.csv',encoding='utf-8',header=True)
