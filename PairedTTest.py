import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("blood_pressure.csv")
# df[['bp_before','bp_after']].describe()

df[['bp_before', 'bp_after']].plot(kind='box')
# This saves the plot as a png file
plt.savefig('boxplot_outliers.png')

df['bp_difference'] = df['bp_before'] - df['bp_after']

df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')
#Again, this saves the plot as a png file
plt.savefig('blood pressure difference histogram.png')

stats.probplot(df['bp_difference'], plot= plt)
plt.title('Blood pressure Difference Q-Q Plot')
plt.savefig('blood pressure difference qq plot.png')

print(stats.shapiro(df['bp_difference']))

print(stats.ttest_rel(df['bp_before'], df['bp_after']))