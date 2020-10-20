import re
import pandas as pd
import numpy as np
import os
from datetime import datetime
from matplotlib import pyplot as plt
data_24=pd.read_csv("C:\MyPrograms\\bhavcopies2\\18-01-2018-TO-17-01-2020ACCEQN (1).csv")
data_24=(pd.pivot_table(data_24,columns=['Date'],values=['Close Price']))
date_string=data_24.columns
lis=[]
## sorting the dates in ascending order
for x in range(len(date_string)):
    lis.append(datetime.strptime(date_string[x],'%d-%b-%Y').date())
data_24.columns=lis
data_24=(data_24.sort_index(axis=1,ascending=True))
plt.plot(data_24.columns,data_24.iloc[0],label='Close Price')
date_input=input("give the input as yyyy-mm-dd for ema30") 
date=(datetime.strptime(date_input,'%Y-%m-%d').date()) ## converting the given date into date format as the index is in the date format
date_loc=(data_24.columns.get_loc(date))
lis.clear()
##calculating ema5
series_type=input("enter the type of series you want")
no_days=int(series_type[3:])##extracting number from string such as 5 from ema5,30 from ema30,etc.
pre_ema=((data_24.iloc[0,no_days]-(np.mean(data_24.iloc[0,0:no_days])))*(2/(no_days+1)))+np.mean(data_24.iloc[0,0:no_days]) ## calculating the ema for the first woking days(no_days)
lis.append(pre_ema)
if(date_loc>=no_days+1):
    for x in range(no_days+1,date_loc+1):
        ema=((data_24.iloc[0,x]-pre_ema)*(2/(no_days+1)))+pre_ema
        lis.append(ema) ##appending the ema for plotting the graph
        pre_ema=ema
print(ema)
## plotting the ema series 
##plt.plot(data_24.columns[no_days:],lis,label='EMA series')
##program for finding the retracement levels
difference=np.max(data_24.iloc[0])-np.min(data_24.iloc[0])
alltime_high=(np.max(data_24.iloc[0]))
alltime_low=(np.min(data_24.iloc[0]))
y=alltime_low+(23.6*difference/(100))
plt.axhline(y=y,label='23.6%',linestyle='dashed')
y=alltime_low+(38.2*difference/(100))
plt.axhline(y=y,label='38.2',color='y',linestyle='dashed')
y=alltime_low+(61.8*difference/(100))
plt.axhline(y=y,label='61.2',color='g',linestyle='dashed')
y=alltime_low+(78.6*difference/(100))
plt.axhline(y=y,label='78.6',color='r',linestyle='dashed')
plt.legend()
plt.show()



## if you we want to plot a ema5,ema30,ema60,etc and retracement level then we can put the whole function in for loop or a while loop
