# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import datetime as datetime
from datetime import timedelta


class Data_Model:

    dfBuga = None
    dfGiron = None
    dfYopal = None

    def __init__(self):
        self.initialize()

    def initialize(self):
        data = pd.read_csv("src/Data.csv")
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Age'] = df['Age'].astype(float)
        df.set_index('Id', inplace=True)
        self.dfBuga = df[df.City == 'Buga']
        self.dfGiron = df[df.City == 'Girón']
        self.dfYopal = df[df.City == 'Yopal']

    def assign_zeros(self, nb_df) :
        day_delta = datetime.timedelta(days=1)
        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date(2020, 1, 1)

        list_values = []
        
        for i in range((end_date - start_date).days):
            date = start_date + i*day_delta
            date2 = date.strftime('%Y-%m-%d')
            try:
                list_values.append(nb_df.at[date2,'Cases'])
            except BaseException as e:
                list_values.append(0)
                
        final_model = pd.DataFrame(columns=('Date', 'Cases'))

        for i in range((end_date - start_date).days):
            date = start_date + i*day_delta
            final_model.loc[len(final_model)]=[date, list_values[i]]
            
        return final_model

    def calculate_hits(self, test, predictions) :
        hits = 0
        for i in range(0, len(predictions)) :
            x = test[i]
            y = predictions[i]
            if(x != 0 and y != 0) :
                if(x == y) :
                    hits += 1
        return hits

    def AR(self, series, nb_name, max_prediciton_size, optime_lags, flag) :

        if(flag):
            fecha_1 = datetime.date(2016, 12, 31)
            fecha_2 = datetime.date(2017, 1, 1)
        else:
            fecha_1 = datetime.date(2015, 12, 31)
            fecha_2 = datetime.date(2016, 1, 1)

        df_train = series.loc[: fecha_1]
        df_test = series.loc[fecha_2: ]

        y1 = df_train.Cases.to_numpy()
        y2 = df_test.Cases.to_numpy()

        # Entrenamiento del modelo
        train, test = y1, y2

        # train autoregression
        window = optime_lags
        model = AutoReg(train, lags=optime_lags, old_names=False)
        model_fit = model.fit()
        coef = model_fit.params
        
        # walk forward over time steps in test
        history = train[len(train)-window:]
        history = [history[i] for i in range(len(history))]
        predictions = list()
        for t in range(len(test)):
            length = len(history)
            lag = [history[i] for i in range(length-window,length)]
            yhat = coef[0]
            for d in range(window):
                yhat += coef[d+1] * lag[window-d-1]
            obs = test[t]
            predictions.append(abs(np.round(float(yhat))))
            history.append(obs)
        test = test[-max_prediciton_size:]
        predictions = predictions[0:max_prediciton_size]
        #rmse = np.sqrt(mean_squared_error(test, predictions))
        real_cases = sum(i for i in test if i != 0) 
        number_of_predictions = sum(1 for i in predictions if i != 0) 
        #hits = self.calculate_hits(test, predictions)
        ans = [list(predictions), list(test), number_of_predictions, real_cases]
        return ans
        
    def get_predictions(self, city, neigborhood, days_to_predict, lags) :
        ans = None
        try:
            flag = False
            if(city == 'Buga') :
                df_neighborhood = self.dfBuga[self.dfBuga.Neighborhood == neigborhood]
                flag = True
            elif(city == 'Yopal') :
                df_neighborhood = self.dfYopal[self.dfYopal.Neighborhood == neigborhood]
            else :
                df_neighborhood = self.dfGiron[self.dfGiron.Neighborhood == neigborhood]
            
            df_neighborhood = pd.DataFrame(df_neighborhood['Date'].value_counts().sort_index())
            df_neighborhood.columns = ['Cases']
            df_neighborhood.index.name = 'Date'
            df_neighborhood = self.assign_zeros(df_neighborhood)
            df_neighborhood.set_index('Date',inplace=True)
            ans = self.AR(df_neighborhood, neigborhood, days_to_predict, lags, flag)

            pred = ans[0]
            test = ans[1]
            number_of_predictions = ans[2]

            day_delta = datetime.timedelta(days=1)

            if(flag) :
                start_date = datetime.date(2017, 1, 1)
            else:
                start_date = datetime.date(2016, 1, 1)

            end_date = start_date + days_to_predict*day_delta
            final_data = []

            for i in range((end_date - start_date).days):
                date = start_date + i*day_delta
                date2 = date.strftime('%Y-%m-%d')
                triple_pred = [date2, 'Predicciones', pred[i]]
                triple_test = [date2, 'Realidad', test[i]]

                final_data.append(triple_pred)
                final_data.append(triple_test)
                
            
            results = [final_data, number_of_predictions]

        except Exception as e:
        
            print("[-]",e)
            results = e

        return results


    
