### DPD Bucket generator ...

## This is under development ...

## Step 0) generate time range function

import numpy as np
import pandas as pd
import datetime

def CreateTimeScale(y0=2016,m0=10,d0=1,yN=2016,mN=12,dN=31,delta_t=28,date_format='%Y-%m'): 
    '''
    Returns a pandas Series encompassing the dates specified in a given range
    '''
    date_0 = datetime.datetime(y0, m0, d0)
    date_N = datetime.datetime(yN, mN, dN)
    dt     = datetime.timedelta(days=delta_t)
    
    dates = []
    string_format = date_format
    
    while date_0 < date_N:
        dates.append(date_0.strftime(string_format))
        date_0 += dt
        
    return pd.to_datetime(pd.Series(np.unique(dates),),format='%Y-%m')
    
## Subset of original dataframe
df_ = df[['fi_acc_id','account_cycle_date','dpd_bucket']]

## Step 1) converts the date column into datetime format

df_['account_cycle_date'] = pd.to_datetime(df_['account_cycle_date'])

## Step 2) defines users and dates

users = np.unique(df_['fi_acc_id'])
dates = CreateTimeScale()
# Specify a minimum period (e.g. months)
dates = dates.dt.to_period('M')

## Step 3) generate new 'year-month' column

df_['month_year'] = df_['account_cycle_date'].dt.to_period('M')

## Step 4) reindex dataframe to include missing points based on year-month column

import pandas as pd
users = np.unique(df_['fi_acc_id'])
idx = pd.MultiIndex.from_product((users,dates), names=['fi_acc_id', 'dt'])
grouped_data = df_.set_index(['fi_acc_id','month_year']).reindex(idx, fill_value=999).reset_index()

## Step 5) summarize dpd bucket information

grouped_data['dpd_bucket'] = grouped_data['dpd_bucket'].apply(lambda x: str(x))
grouped_data['dpd_bucket'] = grouped_data.groupby(['fi_acc_id'])['dpd_bucket'].apply(lambda x: x.cumsum())
grouped_data['dpd_bucket'] = grouped_data['dpd_bucket'].apply(lambda x: x.replace('999','N'))
grouped_data['dpd_bucket'] = grouped_data['dpd_bucket'].apply(lambda x: list(x))










