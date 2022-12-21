import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
import scipy.stats as stats
import statsmodels.stats.api as sms
import warnings
warnings.filterwarnings('ignore')

# Stocks

import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2019,11,30)

tick = 'AAPL'
stock = yf.download(tick,start=start, end=end, progress=False)
stock.columns = stock.columns.str.lower()

stock.close.plot();

import statsmodels.api as sm

sm.graphics.tsa.plot_acf(stock.close, lags = 200);

def diffdf(df:"pd.DataFrame", var:str, interval:int = 1) -> "pd.DataFrame":
    '''
    Takes a dataframe with a var column which is a time series and returns new dataframe
    with a new variable which results from the difference of time t and time t minus interval
    '''
    # internal func
    series = df[var]

    diff = list()
    for i in range(interval, len(series)):
        value = series[i] - series[i - interval]
        diff.append(value)

    diff = pd.Series(diff)

    # new dataframe with only relevant rows to plot
    newdf = df[interval:]

    # final dataframea
    newdf[f'diff_{interval}'] = diff.values

    return newdf

def embed(df:"pd.DataFrame", var:str, m:int, lag:int):

# Embedding

	from gtda.time_series import TakensEmbedding
	
	# embed = TakensEmbedding(time_delay = 3, dimension = 2)
	
	# series = stock['close'].values.reshape(-1,1)
	# series
	
	# embed.fit_transform(X = series)
	
	lag = 15
	_x = stock.close[:-lag]
	# dropa index do segundo
	_y = stock.close[lag:].reset_index(drop=True).values
	dfnew = pd.DataFrame({'x':_x,'y':_y}); x = dfnew.x; y = dfnew.y
	plt.scatter(x,y)

def embed(series:"pd.Series", lag:int, plot:bool = True):
    lag = 15
    _x = series[:-lag]
    # dropa index do segundo
    _y = series[lag:].reset_index(drop=True).values
    dfnew = pd.DataFrame({'x':_x,'y':_y}); x = dfnew.x; y = dfnew.y
    if plot:
        plt.scatter(x=x,y=y)

## Seno

seno = pd.Series(np.sin(range(0,100)))
# plt.plot(seno);
sm.graphics.tsa.plot_acf(seno);

embed(seno,3)

series = seno
lag = 15
_x = series[:-2*lag]
_y = series[lag:-lag].reset_index(drop=True).values
_z = series[2*lag:].reset_index(drop=True).values
dfnew = pd.DataFrame({'x':_x,'y':_y,'z':_z}); x = dfnew.x; y = dfnew.y; z = dfnew.z

### Kaggle - Taken's Embedding

#Full credits on https://www.kaggle.com/tigurius/introduction-to-taken-s-embedding

def takensEmbedding (data, delay, dimension):
    "This function returns the Takens embedding of data with delay into dimension, delay*dimension must be < len(data)"
    if delay*dimension > len(data):
        raise NameError('Delay times dimension exceed length of data!')    
    embeddedData = np.array([data[0:len(data)-delay*dimension]])
    for i in range(1, dimension):
        embeddedData = np.append(embeddedData, [data[i*delay:len(data) - delay*(dimension - i)]], axis=0)
    return embeddedData;

aapl = stock.close.values

embedded = takensEmbedding(aapl, delay = 90, dimension = 6)
embedded

# load some standard libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import math #math fun
import matplotlib.pyplot as plt #plotting
from mpl_toolkits.mplot3d import Axes3D #3d plots
from sklearn.neighbors import NearestNeighbors 

#load weather data that will be used in the script
cityTable     = pd.read_csv('data/city_attributes.csv')
temperatureDF = pd.read_csv('data/temperature.csv', index_col=0)
temperatureDF.index = pd.to_datetime(temperatureDF.index)

#Apply Takens embedding to daily weather data of Montreal
t = pd.date_range(pd.to_datetime('22/6/2015',dayfirst=True),pd.to_datetime('31/8/2015',dayfirst=True),freq='H')
weatherDataMontreal = temperatureDF.loc[t,'Montreal'];
origSignal = weatherDataMontreal;
#we are interested in the daily dynamics, so we have to highpass-filter the signal 
#to remove the monthly and yearly dynamics
#apply rolling mean over one day and plot the signal (low pass filter) 
windowSize = 24
lowPassFilteredSignal = weatherDataMontreal.rolling(windowSize, center=True).mean()
# subtract the low pass filtered singal from the original to get high pass filtered signal
weatherDataMontreal = weatherDataMontreal - lowPassFilteredSignal
#remove all NaNs
weatherDataMontreal = weatherDataMontreal.dropna()
#embedd into two dimensions
embeddedWeather = takensEmbedding(weatherDataMontreal,5,2);
#plot the time-series and the embedded one 
fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(15,14));
ax[0].plot(weatherDataMontreal);
ax[1].plot(embeddedWeather[0,:],embeddedWeather[1,:]);
ax[2].axis('off')
#embed into three dimensions
embeddedWeather3 = takensEmbedding(weatherDataMontreal, 6,3);
#plot the 3D embedding
ax = fig.add_subplot(3, 1, 3, projection='3d')
ax.plot(embeddedWeather3[0,:],embeddedWeather3[1,:],embeddedWeather3[2,:]);

def mutualInformation(data, delay, nBins):
    "This function calculates the mutual information given the delay"
    I = 0;
    xmax = max(data);
    xmin = min(data);
    delayData = data[delay:len(data)];
    shortData = data[0:len(data)-delay];
    sizeBin = abs(xmax - xmin) / nBins;
    #the use of dictionaries makes the process a bit faster
    probInBin = {};
    conditionBin = {};
    conditionDelayBin = {};
    for h in range(0,nBins):
        if h not in probInBin:
            conditionBin.update({h : (shortData >= (xmin + h*sizeBin)) & (shortData < (xmin + (h+1)*sizeBin))})
            probInBin.update({h : len(shortData[conditionBin[h]]) / len(shortData)});
        for k in range(0,nBins):
            if k not in probInBin:
                conditionBin.update({k : (shortData >= (xmin + k*sizeBin)) & (shortData < (xmin + (k+1)*sizeBin))});
                probInBin.update({k : len(shortData[conditionBin[k]]) / len(shortData)});
            if k not in conditionDelayBin:
                conditionDelayBin.update({k : (delayData >= (xmin + k*sizeBin)) & (delayData < (xmin + (k+1)*sizeBin))});
            Phk = len(shortData[conditionBin[h] & conditionDelayBin[k]]) / len(shortData);
            if Phk != 0 and probInBin[h] != 0 and probInBin[k] != 0:
                I -= Phk * math.log( Phk / (probInBin[h] * probInBin[k]));
    return I;

datDelayInformation = []
for i in range(1,21):
    datDelayInformation = np.append(datDelayInformation,[mutualInformation(weatherDataMontreal,i,16)])
plt.plot(range(1,21),datDelayInformation);
plt.xlabel('delay');
plt.ylabel('mutual information');

#embedd into two dimensions
embeddedWeather = takensEmbedding(weatherDataMontreal,5,2);
#plot the time-series and the embedded one 
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(15,14));
ax[0].plot(embeddedWeather[0,:],embeddedWeather[1,:]);
ax[0].set_xlabel('$x_i$');
ax[0].set_ylabel('$x_{i+5}$');
#now with delay=1
embeddedWeather = takensEmbedding(weatherDataMontreal,1,2);
ax[1].plot(embeddedWeather[0,:],embeddedWeather[1,:]);
ax[1].set_xlabel('$x_i$');
ax[1].set_ylabel('$x_{i+1}$');
