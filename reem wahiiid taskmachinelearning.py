# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 22:33:49 2021

@author: DELL
"""

#import libraries to read dataset
import pandas as pd
# import matplotlib to make visualization
import matplotlib.pyplot as plt
#read dataset by make a variable called dataset
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()   #statics about dataset
# sorting by Title of the jobs
dataset.sort_values("Title", inplace = True)
#3.	Clean the data null#duplications
dataset.drop_duplicates(subset ="Title",keep = False, inplace = True)
dataset.dropna(how='all')
   #4.	Count the jobs for each company and display that in order 
x=dataset['Title'].value_counts()
plt.pie(x)
plt.show() 
#x=dataset.iloc[ :,[0]].values  # x must be in matrix not vector
#y=dataset.iloc[:1].values   #to make the data of numbers not strings
# split dataset into train & test
#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=.70)
