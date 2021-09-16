import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


def convert_to_dataframe(df,symbol):
    # Segregate for a specific symbol
    df = df[df['symbol'] == symbol].copy()
    # Create dictionary of required fields i.e open, close, high, low and date
    data_dict = {'open':df['open'].copy(), 'close':df['close'].copy(), 'high':df['high'].copy(), 'low':df['low'].copy(), 'date':df['date'].copy()}
    # Create DataFrame from the dictionary
    nd=pd.DataFrame(data_dict,columns=['open','close','high','low','date'])
    # Fuction call to create chart
    convert_to_olhc_chart(nd,symbol)

def convert_to_olhc_chart(nd,symbol):
    # returns array of evenly spaced numbers from 0 to length of dataframe
    x = np.arange(0,len(nd))
    # The subplots() function takes arguments that describes the layout of the figure.
    # The layout is organized in rows and columns, which are represented by the first and second argument.
    # The figsize attribute allows us to specify the width and height of a figure in unit inches.
    fig, ax = plt.subplots(1, figsize=(12,6))
    idx=0
    # iterrows():Iterate over DataFrame rows as (index, Series) pairs.
    for temp, val in nd.iterrows():
        color = '#2CA453'   #Green color
        # if open is greater than close, then color will be orange
        if val['open'] > val['close']: color= '#F04730'
        # To plot a line for each data record
        plt.plot([x[idx], x[idx]], [val['low'], val['high']],color=color)
        # open marker
        plt.plot([x[idx], x[idx]-0.1],
                 [val['open'], val['open']],
                 color=color)
        # close marker
        plt.plot([x[idx], x[idx]+0.1],
                 [val['close'], val['close']],
                 color=color)
        idx=idx+1
    # Get or set the current tick locations and labels of the x-axis.
    plt.xticks(x[::23], nd.date.dt.date[::23])
    # displays title
    plt.title(symbol, loc='center', fontsize=20)
    # display plot
    plt.show()

# extract json data
df=pd.read_json('Stock List.json')
# get all symbols in ls
ls=df['symbol'].unique()
print(ls)
# Accpet user's  choice
symbol=input("Enter your choice from above list: ")
convert_to_dataframe(df,symbol)
