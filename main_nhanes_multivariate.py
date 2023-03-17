import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

sns.regplot(data = da, x = da['BPXDI1'], y = da['BPXDI2'], fit_reg=False,scatter_kws={'alpha':0.2})

print(da[['BPXSY1','BPXSY2']].dropna().corr())
print(da[['BPXDI1','BPXDI2']].dropna().corr())

sns.jointplot(data = da, x = da['BPXDI1'], y = da['BPXDI2'], kind='hist')
sns.jointplot(data = da, x = da['BPXSY1'], y = da['BPXSY2'], kind='hist')

da['RIAGENDRx'] = da.RIAGENDR.replace({1:'Male',2:'Female'})
sns.FacetGrid(da, col="RIDRETH1", row='RIAGENDRx').map(plt.scatter,'BPXSY1','BPXDI1').add_legend()

da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know"})
plt.figure(figsize=(12,4))
sns.violinplot(data=da, x = 'DMDEDUC2x', y = 'RIDAGEYR', hue='RIAGENDRx')

da['agegroup'] = pd.cut(da.RIDAGEYR,[18,30,40,50,60,70,80])
plt.figure(figsize=(12,4))
sns.violinplot(data=da, x = 'agegroup', y = 'BMXBMI', hue='RIAGENDRx')
plt.show()

da["RIDRETH1x"] = da.RIDRETH1.replace({1: "Mexican American", 2: "Other Hispanic", 3: "Non-Hispanic White", 4: "Non-Hispanic Black", 5: "Other Race - Including Multi-Racial"})
da["HIQ210x"] = da.HIQ210.replace({1: "Yes", 2: "No", 7: "Refused", 9: "Don't Know"})

db = da.loc[(da.HIQ210x != 'Refused') & (da.HIQ210x != "Don't Know"),:]
x = pd.crosstab(db.RIDRETH1x,db.HIQ210x)
norm_x = x.apply(lambda z: z/z.sum(), axis = 1).unstack()
print(norm_x)
