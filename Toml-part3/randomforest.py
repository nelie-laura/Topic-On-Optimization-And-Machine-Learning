# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:30:20 2022

@author: Marco-PC
"""

import sklearn.ensemble as ens

from base import Algorithm, Model

class RandForestRegression(Algorithm):
    def __init__(self,data,percentual,predictLabel,alpha=1,gamma=None,scale=False):
        super().__init__(data, percentual,predictLabel,alpha=alpha,scale=scale)
        
    def makeModel(self,numEst,labels=[]):
        return RandForestModel(self.trainingSet,self.trainingLabels,self.testSet,self.testLabels,modelType=self.modelType,alpha=self.alpha,numEst=numEst,selectedLabels=labels)
      
class RandForestModel(Model):
    def __init__(self, trainingSet, trainingLabels, testSet, testLabels,modelType="Normal", alpha=1,numEst=1,selectedLabels=[]):
        super().__init__(trainingSet, trainingLabels, testSet, testLabels,modelType=modelType, alpha=alpha,selectedLabels=selectedLabels)
        
        self.model=None
        self.numEst=numEst
        self.model=ens.RandomForestRegressor(n_estimators=self.numEst)
        self.redefineSets()
        #self.model.fit(self.trainingSet,self.trainingLabels)
        #select=forwardSelection(self.model)
        #self.model.fit(self.trainingSet,self.trainingLabels)
        #select.fit(trainingSet,trainingLabels)
        #self.featuresSelected=np.array(self.trainingSet.columns[select.get_support()])
        #self.trainingSet=self.makeDataset(self.featuresSelected,select.transform(self.trainingSet).T)
        #self.testSet=self.makeDataset(self.featuresSelected,select.transform(self.testSet).T)
        
        
        self.model.fit(self.trainingSet,self.trainingLabels)
        
        #self.features=self.model.transform(self.trainingSet)
    def params(self):
        return {
            "n_estimators":[1,2,5,10],
            "criterion":["squared_error","absolute_error","poisson"],
            "max_depth":[None,1,2,5,10],
            "min_samples_split":[1,2,5,10],
            "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10],
            "max_features":["sqrt","log2",None,1,2,3,0.7],
            "max_leaf_nodes":[None,1,2,3,4,5],
            "max_samples":[None,1,2,3,4,5,0.7,0.3]
            }
    
    
        