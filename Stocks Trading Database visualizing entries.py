import glob
import pandas as pd
from pandas import read_csv
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import plotly.express as px
import plotly.graph_objects as go
import os
from IPython.display import display, Image


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

#find the entries

big_frame = big_frame.loc[big_frame['entry/exit']=='entry']
big_frame = big_frame.replace('entry',1)

#bar graph done with PlotLy

df = big_frame

fig = go.Figure()

fig.add_trace(go.Bar(
    name="Middle-aligned",
    x=df["time"], y=df["entry/exit"],
    xperiod="M1",
    xperiodalignment="middle"
))
fig.update_xaxes(showgrid=True, ticklabelmode="period")


#Ticker + Graph finder

csv_directory = '/Users/cindymendoncapaez/Downloads/Breakout US stocks/breakout/csv/'

@interact
def show_csv(file=os.listdir(csv_directory)):
    display(pd.read_csv(csv_directory+file, sep = ';'))
    code = file.split('.csv')[0]

fdir = '/Users/cindymendoncapaez/Downloads/Breakout US stocks/breakout/graphs/'

@interact
def show_images(ticker_name = code):
    list_code = os.listdir(fdir)
    list_match = [x for x in list_code if x.startswith(ticker_name + '_')]
    for file in list_match:
        display(Image(fdir+file))
 
#Plotly line graph

path = '/Users/cindymendoncapaez/Downloads/Breakout US stocks/breakout/csv/'

global code

@interact
def show_csv(file=os.listdir(path)):
    global tickers
    tickers = pd.read_csv(path+file, sep = ';')
    code = file.split('.csv')[0]

    
@interact
def display_time_series(param = tickers):
    list_code = os.listdir(path)
    list_match = [x for x in list_code if x.startswith(param + '_')]
    fig = px.line(tickers, x=tickers['time'], y=param) 
    fig.show()


#Values

days_high = tickers["high"]
days_low = tickers["low"]
days_close = tickers["close"]

daily_ranges = []

for ticker in tickers:

    profit = (days_low + days_high) /2
   
combined_data = tickers
combined_data['entry_price'] =  entry_price
combined_data['exit_price'] = exit_price

#First entry & Last exit code. Please notice that the underlined rows are the ones to look at.

@interact
def show_csv(file=os.listdir(csv_directory)):
    tickers = pd.read_csv(path+file, sep = ';')
    combined_data = tickers
    combined_data['entry_price'] =  entry_price
    combined_data['exit_price'] = exit_price
    last_exit = combined_data.groupby(['entry/exit'], as_index='exit').last()
    first_entry = combined_data.groupby(['entry/exit'], as_index='entry').first()
    last_exit_style = last_exit.style.set_properties(subset = pd.IndexSlice[['exit'], :], **{'background-color' : 'yellow'})
    first_entry_style = first_entry.style.set_properties(subset = pd.IndexSlice[['entry'], :], **{'background-color' : 'yellow'})
 

display (first_entry_style)
display (last_exit_style)
print(big_frame)
print(combined_data)
