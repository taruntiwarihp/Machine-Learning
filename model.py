import pandas as pd
import numpy
import matplotlib.pyplot as plt


data = pd.read_csv('train.csv')
meal_info = pd.read_csv('meal_info.csv')
print(data.head())
print(meal_info)