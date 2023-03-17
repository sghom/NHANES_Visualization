import numpy as np
import pandas as pd

pd.set_option('display.max_columns',100)

df = pd.read_csv('nhanes_2015_2016.csv')
print(df.columns)
keep = []
for column in df.columns:
    if 'BMX' in column:
        keep.append(column)

print(keep)

df_BMX  = df[keep]
print(df_BMX.head())

print(df.loc[:,keep].head())

index_bool = np.isin(df.columns,keep)
print(index_bool)

print(df.loc[:,index_bool].head())

waist_median = pd.Series.median(df_BMX['BMXWAIST'])
print(waist_median)
print(df_BMX[df_BMX['BMXWAIST'] > waist_median].head())

condition_1 = df_BMX['BMXWAIST'] > waist_median
condition_2 = df_BMX['BMXLEG'] < 32
print(df_BMX[condition_1 & condition_2].head())

print(df_BMX.loc[condition_1 & condition_2,:].head())