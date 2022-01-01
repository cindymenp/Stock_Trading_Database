# Stock_Trading_Database

This database contains data of a specific technical analysis setup in stock trading. The setup is based on Kristjan Kullamagi's trading strategy (qullamaggie.com) and it's called the high tight flag. The database its purpose is to train a trader's ability to recognise valid setups. It will show charts with drawings where setups occur, captured from TradingView software. Also it shows tables with the open high low close & indicator data of the relevant stocks. Furthermore there is code for several statistical methods to give more insight.

# Libraries

## glob

The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.

#### Usage ####

```` 

filenames = glob.glob(path + "/*.csv")

```` 

## ipywidgets

Also known as jupyter-widgets or simply widgets, are interactive HTML widgets for Jupyter notebooks and the IPython kernel.

#### Usage ####

```` 

@interact
def show_csv(file=os.listdir(csv_directory)):
    display(pd.read_csv(csv_directory+file, sep = ';'))
    code = file.split('.csv')[0]

@interact
def show_images(ticker_name = code):
    list_code = os.listdir(fdir)
    list_match = [x for x in list_code if x.startswith(ticker_name + '_')]
    for file in list_match:
        display(Image(fdir+file))
        
 --
 
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

```` 

## plotly.express

The plotly.express module (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or PX. 

#### Usage ####

    fig = px.line(tickers, x=tickers['time'], y=param) 
    fig.show()

## plotly.graph_objects 

The figures created, manipulated and rendered by the plotly Python library are represented by tree-like data structures which are automatically serialized to JSON for rendering by the Plotly.js JavaScript library. 

#### Usage ####

```` 

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

```` 

## os

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. 

#### Usage ####

```` 

def show_csv(file=os.listdir(csv_directory)):
    display(pd.read_csv(csv_directory+file, sep = ';'))
    code = file.split('.csv')[0]

def show_images(ticker_name = code):
    list_code = os.listdir(fdir)
    list_match = [x for x in list_code if x.startswith(ticker_name + '_')]
    for file in list_match:
        display(Image(fdir+file))
        

def show_csv(file=os.listdir(path)):
    global tickers
    tickers = pd.read_csv(path+file, sep = ';')
    code = file.split('.csv')[0]

    
def display_time_series(param = tickers):
    list_code = os.listdir(path)
    list_match = [x for x in list_code if x.startswith(param + '_')]
    fig = px.line(tickers, x=tickers['time'], y=param) 
    fig.show()

```` 

## IPython.display

When this object is returned by an input cell or passed to the display function, it will result in Image controls being displayed in the frontend (only works in the notebook).

#### Usage ####

```` 

def show_csv(file=os.listdir(csv_directory)):
    display(pd.read_csv(csv_directory+file, sep = ';'))
    code = file.split('.csv')[0]

def show_images(ticker_name = code):
    list_code = os.listdir(fdir)
    list_match = [x for x in list_code if x.startswith(ticker_name + '_')]
    for file in list_match:
        display(Image(fdir+file))
```` 
        
# Installation of all libraries

Use for all libraries the package manager pip to install .

## glob

Termial:

Python 2: pip install glob //Python 3: pip3 install glob

Jupyter Lab:

Python 2: %pip install glob //Python 3: %pip3 install glob

## ipywidgets

Termial:

Python 2: pip install ipywidgets//Python 3: pip3 install ipywidgets

Jupyter Lab:

Python 2: %pip install ipywidgets //Python 3: %pip3 install ipywidgets

## plotly.express

Termial:

Python 2: pip install plotly-express//Python 3: pip3 install plotly-express

Jupyter Lab:

Python 2: %pip install plotly-express //Python 3: %pip install plotly-express

## plotly.graph_objects 

Termial:

Python 2: pip install plotly //Python 3: pip3 install plotly

Jupyter Lab:

Python 2: %pip install plotly //Python 3: %pip3 install plotly

## os

Termial:

Python 2: pip install os-sys //Python 3: pip3 install os-sys

Jupyter Lab:

Python 2: %pip install os-sys //Python 3: %pip3 install os-sys


## IPython.display

Termial:

Python 2: pip install ipython //Python 3: pip3 install ipython

Jupyter Lab:

Python 2: %pip install ipython //Python 3: %pip3 install ipython

