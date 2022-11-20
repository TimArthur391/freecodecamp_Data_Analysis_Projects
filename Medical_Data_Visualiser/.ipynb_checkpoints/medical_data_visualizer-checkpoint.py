import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight']/((df['height']*0.01) ** 2)
df['overweight'] = pd.Series(np.where(BMI.values > 25, 1, 0), BMI.index)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = pd.Series(np.where(df['cholesterol'].values > 1, 1, 0), df['cholesterol'].index)
df['gluc'] = pd.Series(np.where(df['gluc'].values > 1, 1, 0), df['gluc'].index)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat.rename(columns = {'value':'cardio'}, inplace = True)
    df_cat = df_cat.groupby(["cardio","variable"]).size().reset_index(name='count') 

    # Draw the catplot with 'sns.catplot()'
    sns_plot = sns.catplot(df_cat, y='count', x='variable', col='cardio', kind="bar")



    # Get the figure for the output
    fig = sns_plot


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
             (df['height'] >= df['height'].quantile(0.025)) &
             (df['height'] <= df['height'].quantile(0.975)) &
             (df['weight'] >= df['weight'].quantile(0.025)) &
             (df['weight'] <= df['weight'].quantile(0.975))
            ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.full((14, 14), True))



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr.mask(mask), annot=True, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
