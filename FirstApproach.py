# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:22:59 2018

@author: manel.serrano
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.style.use('ggplot')

train = pd.read_csv("Datasets/train.csv", sep = ",")
test = pd.read_csv("Datasets/test.csv", sep = ",")
combine = [test, train]

def supervivenciaPorSexo(dataSet):
  sns.barplot(x="Sex", y="Survived", data=dataSet)
  print("Porcentaje de hombres que sobrevivieron: ", 
        dataSet["Survived"][dataSet["Sex"] == 'male'].value_counts(normalize = True)[1]*100)
  print("Porcentaje de mujeres que sobrevivieron: ", 
        dataSet["Survived"][dataSet["Sex"] == 'female'].value_counts(normalize = True)[1]*100)

def histogramaEdades(dataSet):
  sns.distplot(dataSet.loc[dataSet["Age"].notnull(),"Age"])
  
def createTitle(dataSet):
    for data in dataSet:
      data["Title"] = data.Name.str.extract("([A-Za-z]+)\.", expand = False)

def groupTitles(dataSet):
  
  
def main():
  """
  supervivenciaPorSexo(train)
  histogramaEdades(train)
  """
  createTitle(combine)
  


if __name__ == '__main__':
  main()