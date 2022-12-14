import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')
    # Create scatter plot
    x = df.index
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    
    # Create first line of best fit
    res = linregress(x, y=y)
    linregress_x = np.append(x.to_numpy(), np.arange(2014, 2051))
    plt.plot(linregress_x, res.intercept + res.slope*linregress_x, 'r', label='fitted line')
    
    # Create second line of best fit
    x_2 = df.index.where(df.index >= 2000).dropna()
    y_2 = df.loc[2000:]['CSIRO Adjusted Sea Level']
    res_2 = linregress(x_2, y=y_2)
    linregress_x_2 = np.arange(2000, 2051)
    plt.plot(linregress_x_2, res_2.intercept + res_2.slope*linregress_x_2, 'g', label='fitted line')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()