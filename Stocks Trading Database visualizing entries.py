import glob
import pandas as pd
from pandas import read_csv
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import plotly.express as px
import plotly.graph_objects as go
import os
from IPython.display import display, Image
import numpy as np

# get data file names
path =r'/Users/cindymendoncapaez/opt/anaconda3/lib/python3.8/site-packages/folium/finance project/Breakout US stocks' 
filenames = glob.glob(path + "/*.csv")

dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

#set the column names
big_frame.columns = ['time', 'open', 'high', 'low', 'close', 'MA50', 'MA20', 'MA10', 'ADR', 'DV M', 'MA20 DV M', 'entry/exit']
big_frame


#file=os.listdir(csv_directory)):
#tickers = pd.read_csv(path+file, sep = ',')
combined_data = big_frame
#combined_data.columns = ['time', 'open', 'high', 'low', 'close', 'MA50', 'MA20', 'MA10', 'ADR', 'DV M', 'MA20 DV M', 'entry/exit'] 
#days_high = tickers["high"]
#days_low = tickers["low"]
#days_close = tickers["close"]
combined_data = combined_data[combined_data['entry/exit'].isin(["entry","exit"])]
combined_data['entry_price']= np.NaN
combined_data['exit_price'] = np.NaN    
combined_data['profit'] = np.NaN
combined_data['risk'] = np.NaN
combined_data['R'] = np.NaN
combined_data.loc[combined_data['entry/exit'].isin(["entry"]), 'entry_price'] = (combined_data['low'] + combined_data['high']) /2
combined_data.loc[combined_data['entry/exit'].isin(["exit"]), 'exit_price'] = combined_data['close']
combined_data['entry_price'] = combined_data['entry_price'].fillna(method='ffill')
combined_data.loc[combined_data['entry/exit'].isin(["exit"]), 'profit'] = combined_data['exit_price']-combined_data['entry_price']
combined_data.loc[combined_data['entry/exit'].isin(["entry"]),'risk'] = combined_data['entry_price']-combined_data['low']
combined_data['risk'] = combined_data['risk'].fillna(method='ffill')
combined_data.loc[combined_data['entry/exit'].isin(["exit"]), 'R'] = combined_data['profit']/combined_data['risk']
    
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.go_offline()
    
combined_data.drop(combined_data[combined_data['entry/exit'] == 'entry'].index, inplace=True)
combined_data.iplot(kind='scatter',x='ADR',y='R',mode='markers',size=10)

#find the entries

big_frame = big_frame.loc[big_frame['entry/exit']=='entry']
big_frame = big_frame.replace('entry',1)
big_frame

df = big_frame

fig = go.Figure()

fig.add_trace(go.Bar(
    name="Middle-aligned",
    x=df["time"], y=df["entry/exit"],
    xperiod="M1",
    xperiodalignment="middle"
))
fig.update_xaxes(showgrid=True, ticklabelmode="period")
fig.show()

csv_directory = 'C:/Users/baszo/Desktop/Breakout US stocks/A/'

@interact
def show_csv(file=os.listdir(csv_directory)):
    global code
    display(pd.read_csv(csv_directory+file, sep = ','))
    code = file.split('.csv')[0]

fdir = '/Users/cindy/Desktop/Breakout US stocks/A/images/'

@interact
def show_images(ticker_name = code):
    list_code = os.listdir(fdir)
    list_match = [x for x in list_code if x.startswith(ticker_name + '_')]
    for file in list_match:
        display(Image(fdir+file))
        
        
 path = '/Users/cindy/Desktop/Breakout US stocks/A/'

@interact
def show_csv(file=os.listdir(path)):
    global tickers
    tickers = pd.read_csv(path+file, sep = ',')
    code = file.split('.csv')[0]

    
@interact
def display_time_series(param = tickers):
    list_code = os.listdir(path)
    fig = px.line(tickers, x=tickers['time'], y=param) 
    fig.show()


