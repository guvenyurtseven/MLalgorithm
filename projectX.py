import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importing Machine Learning Libraries

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("D:/csv files/NFLX_modified.csv",sep = ",", encoding='latin-1')

x_columns=[1,2,3,4,5,6,7,8]

date= df.Date.values.reshape(-1,1)
open= df.Open.values.reshape(-1,1)
high= df.High.values.reshape(-1,1)
low= df.Low.values.reshape(-1,1)
close= df.Close.values.reshape(-1,1)
adj_close= df.AdjClose.values.reshape(-1,1)
volume= df.Volume.values.reshape(-1,1)


Prediction =df.Predicted.values.reshape(-1,1)

# Select the metric to visualize - for example, 'Close' price
metric = 'Close'

# Check if the metric exists in the DataFrame
if metric in df.columns:
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df[metric], label=metric)
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.title(f'{metric} over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
    plt.tight_layout()

    # Display the plot
    plt.show()
else:
    print(f"The metric '{metric}' does not exist in the CSV file.")
