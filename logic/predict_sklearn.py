import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from logic.get_data import *
import ta.trend


async def predict(ticker):
    data =  await get_data_aiomoex(ticker)
    predict_ = predict_one(data)
    trand = get_trand(data)

    if predict_[0] > predict_[1] and trand:
          return "STRONG BUY"
    else:
          if predict_[0] > predict_[1] and trand == False:
                return "BUY"
          else:
                return "DONT BUY"
    
    
def predict_one(data):
        projection = 2

        data = data.iloc[:, 1:]

        data['predict'] = data['close'].shift(-projection)

        x = data[['close']]
        y = data['predict']

        x = x[:-projection]
        y = y[:-projection]

        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,shuffle=False)

        model = LinearRegression()
        model.fit(x_train,y_train)

        return model.predict(data[['close']][-projection:])[-1:],data['close'].values[-1:]
    
def get_trand(data):
    ema_100 = ta.trend.ema_indicator(close = data['close'],
                                             window = 100)[0:].values[-1:]
        
    ema_200 = ta.trend.ema_indicator(close = data['close'],
                                             window = 200)[0:].values[-1:]
    if ema_100 > ema_200:
            return True
    else:
            return False



