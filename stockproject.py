##main method below

import re
import pandas as pd
import numpy as np
from datetime import datetime
import os
csv_files=os.listdir("C:\MyPrograms\\bhavcopies1")
csv_dates=[]
c=0
## collecting the dates in the format fo/date/year/bhav and converting the into date/year format and sorting them

for x in csv_files:
    csv_dates.append(x[x.find("fo")+2:x.find("bhav")])
for x in range(len(csv_dates)):
    for y in  range(len(csv_dates)-1):
        if(datetime.strptime(csv_dates[x],"%d%b%Y")>datetime.strptime(csv_dates[y],"%d%b%Y")):
            temp=csv_dates[x]
            csv_dates[x]=csv_dates[y]
            csv_dates[y]=temp
csv_files=csv_dates

for bhavcopy_date in csv_files:
    file_dates=open("closing_dates.txt","r")  ##file dates consists of the series  i.e dates for december series,dates for november series,etc.
    for date in file_dates.readlines():##iterating through series
        ranges=re.split("-",date)
        if(datetime.strptime(ranges[0].rstrip("\n"),"%d%b%Y")<=(datetime.strptime(bhavcopy_date,"%d%b%Y"))):##comparing the datetime objects
            if(datetime.strptime(ranges[1].rstrip("\n"),"%d%b%Y")>=(datetime.strptime(bhavcopy_date,"%d%b%Y"))):
                 bhav_copy=pd.read_csv("C:\MyPrograms\\bhavcopies1\\"+"fo"+bhavcopy_date+"bhav.csv")##reading the bhavcopy
                 todays_date=bhav_copy.ix[0,'TIMESTAMP']
                 bhav_copy = bhav_copy[(bhav_copy['OPTION_TYP']=='XX') & (bhav_copy['EXPIRY_DT']==(ranges[1][:2]+'-'+ranges[1][2:5]+'-'+ranges[1][5:]).rstrip("\n"))].reset_index(drop=True).ix[:,['INSTRUMENT','SYMBOL','CLOSE']]
                 bhav_copy.rename(columns={'CLOSE':todays_date},inplace=True)

                 if(c==0):
                    saving_bhavcopy1=bhav_copy
                 if(c==1):
                    final_file=pd.merge(bhav_copy,saving_bhavcopy1,on=['INSTRUMENT','SYMBOL'],how='inner')
                 if(c>1):
                    final_file=pd.merge(bhav_copy,final_file,on=['INSTRUMENT','SYMBOL'],how='inner')
                 c=c+1
print(final_file)
export_csv=final_file.to_csv('final_file.csv',encoding='utf-8',header=True)

## to calculate ema5,ema10,ema20,ema60
##print(final_file['SYMBOL'])
##x=input("enter the date for which you want ema5")
##print("to find the ema5 of banknifty on 31-dec-2019")
##y=final_file.columns.get_loc(x)
##print(y)
##print((final_file.ix[0,y+1:y+6]))
##print(final_file)
##print(final_file.iat[0,y])
##row=final_file[final_file['SYMBOL']=='BANKNIFTY'].index.values
##print(type(row))
##ema5=(final_file.iat[row,y]-(np.mean(final_file.ix[row,y+1:y+6])*(2/(5+1))))+np.mean(final_file.ix[row,y+1:y+6])
##print(ema5)







            
        
               
