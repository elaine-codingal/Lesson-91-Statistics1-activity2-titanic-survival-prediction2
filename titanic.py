#Import required libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data=pd.read_csv('Titanic Dataset.csv')

print(data.head())

#Median value of age and fare
median_age=np.median(data['Age'])
print("Median value of age-", median_age)

median_fare=np.median(data['Fare'])
print("Median value of fare -", median_fare)

"""###**Mode value of Age and Pclass**"""
mode_age=stats.mode(data['Age'])
print("Mode value of age -", mode_age)

mode_class=stats.mode(data['Pclass'])
print("Mode value of class -", mode_class)

"""###**Mode value of Categorical Feature - Gender**"""
mode_gender=data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)




