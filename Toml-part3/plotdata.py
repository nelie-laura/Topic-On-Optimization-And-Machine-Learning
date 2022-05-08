# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:29:36 2022

@author: Marco-PC
"""

from base import prepareData
import dplotter as dp
import numpy as np

def sensorData():
    listfiles=["captor17013-sensor1.csv",
               "NO_Manlleu.csv",
               "PM10_Manlleu.csv",
               "SO2_Manlleu.csv",
               "NO2_Manlleu.csv"]
    return prepareData(listfiles, ";")

data=sensorData()
delete=False
for ptype in dp.plotTypes():
    p=dp.Plotter()
    y=data["Temp"]
    x=np.arange(0,len(y),1)
    p.show(ptype,x, y)