import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

da = pd.read_csv("nhanes_2015_2016.csv")

sns.regplot(data = da, x='BMXLEG', y= 'BMXARML', fit_reg=False,scatter_kws={'alpha':0.2})
sns.jointplot(data = da, x='BMXLEG', y= 'BMXARML', kind ='hist')

da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
sns.FacetGrid(da, col = 'RIAGENDRx').map(plt.scatter, "BMXLEG",'BMXARML', alpha = 0.4).add_legend()

print(da.loc[da.RIAGENDRx=='Female',['BMXLEG','BMXARML']].dropna().corr())
print(da.loc[da.RIAGENDRx=='Male',['BMXLEG','BMXARML']].dropna().corr())

sns.FacetGrid(da, col="RIDRETH1", row='RIAGENDRx').map(plt.scatter,'BMXLEG','BMXARML',alpha=0.2).add_legend()

da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know"})
da["DMDMARTLx"] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married", 6: "Living w/partner", 77: "Refused"})

db = da.loc[(da.DMDEDUC2x != "Don't Know") & (da.DMDMARTLx != 'Refused'),:]

x = pd.crosstab(db.DMDEDUC2x,db.DMDMARTLx)
norm = x.apply(lambda z: z/z.sum(), axis = 1)

print(db.groupby(['RIAGENDRx','DMDEDUC2x','DMDMARTLx']).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis=1))