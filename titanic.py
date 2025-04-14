#Import required libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data=pd.read_csv('Titanic_Dataset.csv')

print(data.head(5))

#Mean value of age
mean_age=np.mean(data['Age'])
print("Mean Age is - ", mean_age)

#Mean value of fare
mean_fare=np.mean(data['Fare'])
print("Mean Fare is - ",mean_fare)




