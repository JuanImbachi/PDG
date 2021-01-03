# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from model.data_model import Data_Model
from .models import DengueCase
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import datetime as datetime
from datetime import timedelta

import unittest

class TestModels(TestCase) :

    dfBuga = None
    dfGiron = None
    dfYopal = None

    def initialize(self):
        data = pd.read_csv("src/Data.csv")
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Age'] = df['Age'].astype(float)
        df.set_index('Id', inplace=True)
        self.dfBuga = df[df.City == 'Buga']
        self.dfGiron = df[df.City == 'Girón']
        self.dfYopal = df[df.City == 'Yopal']
    
    #Methods to get the data of a neighborhood
    def update_buga(self, neigborhood) :
        self.df_neighborhood = self.dfBuga[self.dfBuga.Neighborhood == neigborhood]

    def update_giron(self, neigborhood) :
        self.df_neighborhood = self.dfGiron[self.dfGiron.Neighborhood == neigborhood]

    def update_yopal(self, neigborhood) :
        self.df_neighborhood = self.dfYopal[self.dfYopal.Neighborhood == neigborhood]

    # Method to transform the data to be used in AR model
    def general(self) :
        self.df_neighborhood = pd.DataFrame(self.df_neighborhood['Date'].value_counts().sort_index())
        self.df_neighborhood.columns = ['Cases']
        self.df_neighborhood.index.name = 'Date'
        self.df_neighborhood = Data_Model.assign_zeros(self, self.df_neighborhood)
        self.df_neighborhood.set_index('Date',inplace=True)

    def setUp_db (self):
        DengueCase.objects.create(City="Popayán", NotificationDate="2021-01-02", Age="21", Gender="M", Neighborhood="Las Mercedes", Commune="3")

    # BUGA TEST
    def test_Assign_Zeros_Buga_SantaBarbara (self):
        print("[+]", "test_Assign_Zeros_Buga_SantaBarbara")
        try :
            self.initialize()
            self.update_buga('SANTA BARBARA')

            self.df_neighborhood = pd.DataFrame(self.df_neighborhood['Date'].value_counts().sort_index())
            self.df_neighborhood.columns = ['Cases']
            self.df_neighborhood.index.name = 'Date'

            self.df_neighborhood = Data_Model.assign_zeros(self, self.df_neighborhood)
            self.df_neighborhood.set_index('Date',inplace=True)

            results = Data_Model.assign_zeros(self, self.df_neighborhood)

            self.assertEquals(len(results), 3652)
        except :
            self.fail("test_Assign_Zeros_Buga_SantaBarbara, FAILED")
    
    def test_AR_Buga_SantaBarbara  (self) :
        print("[+]", "test_AR_Buga_SantaBarbara")
        try :
            self.initialize()
            self.update_buga('SANTA BARBARA')
            self.general()

            results = Data_Model.AR(self, self.df_neighborhood, 120, 300, 250, True)

            self.assertIsNotNone(results)
        except :
            self.fail("test_AR_Buga_SantaBarbara, FAILED")

    def test_fail_AR_Buga_santabarbara (self) :
        print("[+]", "fail_test_AR_Buga_santabarbara")
        try :
            self.initialize()
            self.update_buga('SANTA BARBARA')
            self.general()

            results = Data_Model.AR(self, self.df_neighborhood, 120, 300, 1, True)

            self.fail("fail_test_AR_buga_santabarbara, FAILED")
        except :
            self.assertTrue(True)

    # YOPAL TEST
    def test_Assign_Zeros_Yopal_Esperanza (self):
        print("[+]", "test_Assign_Zeros_Yopal_Esperanza")
        try :
            self.initialize()
            self.update_buga('ESPERANZA')

            self.df_neighborhood = pd.DataFrame(self.df_neighborhood['Date'].value_counts().sort_index())
            self.df_neighborhood.columns = ['Cases']
            self.df_neighborhood.index.name = 'Date'

            self.df_neighborhood = Data_Model.assign_zeros(self, self.df_neighborhood)
            self.df_neighborhood.set_index('Date',inplace=True)

            results = Data_Model.assign_zeros(self, self.df_neighborhood)

            self.assertEquals(len(results), 3652)
        except :
            self.fail("test_Assign_Zeros_Yopal_Esperanza, FAILED")
    
    def test_AR_Yopal_Esperanzaa (self) :
        print("[+]", "test_AR_Yopal_Esperanzaa")
        try :
            self.initialize()
            self.update_buga('ESPERANZA')
            self.general()

            results = Data_Model.AR(self, self.df_neighborhood, 500, 420, 120, False)

            self.assertIsNotNone(results)
        except :
            self.fail("test_AR_Yopal_Esperanzaa, FAILED")

    def test_fail_AR_Yopal_Esperanza (self) :
        print("[+]", "fail_test_AR_Yopal_Esperanza")
        try :
            self.initialize()
            self.update_buga('ESPERANZA')
            self.general()

            results = Data_Model.AR(self, self.df_neighborhood, 500, 420, 1, False)

            self.fail("fail_test_AR_Yopal_Esperanza, FAILED")
        except :
            self.assertTrue(True)

    # GIRON TEST
    def test_Assign_Zeros_Giron_ElPoblado (self):
        print("[+]", "test_Assign_Zeros_Giron_ElPoblado")
        try :
            self.initialize()
            self.update_buga('EL POBLADO')

            self.df_neighborhood = pd.DataFrame(self.df_neighborhood['Date'].value_counts().sort_index())
            self.df_neighborhood.columns = ['Cases']
            self.df_neighborhood.index.name = 'Date'

            self.df_neighborhood = Data_Model.assign_zeros(self, self.df_neighborhood)
            self.df_neighborhood.set_index('Date',inplace=True)

            results = Data_Model.assign_zeros(self, self.df_neighborhood)

            self.assertEquals(len(results), 3652)
        except :
            self.fail("test_Assign_Zeros_Giron_ElPoblado, FAILED")
    
    def test_AR_Giron_ElPoblado (self) :
        print("[+]", "test_AR_Giron_ElPoblado")
        try :
            self.initialize()
            self.update_buga('EL POBLADO')
            self.general()
            
            results = Data_Model.AR(self, self.df_neighborhood, 350, 330, 230, False)

            self.assertIsNotNone(results)
        except :
            self.fail("test_AR_Giron_ElPoblado, FAILED")

    def test_fail_AR_Giron_ElPoblado (self) :
        print("[+]", "fail_test_AR_Giron_ElPoblado")
        try :
            self.initialize()
            self.update_buga('EL POBLADO')
            self.general()

            results = Data_Model.AR(self, self.df_neighborhood, 350, 330, 1, False)
            
            self.fail("fail_test_AR_Giron_ElPoblado, FAILED")
        except :
            self.assertTrue(True)

    # Add element to DB
    def test_Add_Element_DB (self) :
        print("[+]", "test_Add_Element_DB")
        try :
            DengueCase.objects.create(City="Palmira", NotificationDate="2021-01-02", Age="21", Gender="M", Neighborhood="Las Mercedes", Commune="3")

            self.assertEquals(DengueCase.objects.get(pk=1).City, "Palmira")
        except :
            self.fail("test_Add_Element_DB, FAILED")

    # Delete element from DB
    def test_Delete_Element_DB (self) :
        print("[+]", "test_Delete_Element_DB")
        try :
            self.setUp_db()
            self.assertEquals(DengueCase.objects.get(pk=2).City, "Popayán")

            case = DengueCase.objects.get(pk=2)
            case.delete()

            self.assertEquals(len(DengueCase.objects.all()), 0)
        except :
            self.fail("test_Delete_Element_DB, FAILED")
