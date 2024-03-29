# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:48:10 2022

@author: Marco-PC
"""

from kernel import KernelRegression
import base as b

def sensorData():
    listfiles=["captor17013-sensor1.csv",
               "NO_Manlleu.csv",
               "SO2_Manlleu.csv",
               "NO2_Manlleu.csv"
               #"PM10_Manlleu.csv"
               ]
    return b.prepareData(listfiles, ";")


predLabel="RefSt"
#otherLabel="Sensor_O3"

kernel="rbf"

first=["Sensor_O3","Temp","Sensor_SO2"] #best positives
second=["RelHum","Sensor_NO2","Sensor_NO"] #best negatives
third=["Sensor_O3","Temp","RelHum"] #best squares

features=[first,second,third]

for feature in features:
    print("\n\n\n"+kernel+" KERNEL RIDGE REGRESSION\n\n\n")
    data=sensorData()
    data=data.drop(["date"],axis=1) 
    kernelRegr=KernelRegression(data,0.7,predLabel)
    model=kernelRegr.makeModel(kernel,features=feature)
    model.tune()
    res=model.predict()
    res.printRes()
    model.plot()
