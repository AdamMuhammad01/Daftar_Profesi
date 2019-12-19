import numpy as np
import pandas as pd

a = pd.read_csv('profesi.csv',sep='|')


############1 Dataset Occupation

b = a['occupation'].value_counts()
print(len(b))
print(b.index.tolist())



###########2 dataframe usia maksimal, minimal & rata-ratanya, berdasarkan profesi & gender

c = a.groupby([a['occupation'],a['gender']]).describe()
d = c['age'][['max','min','mean']]
c.rename(columns={'max':'max_usia','min':'min_usia','mean':'rerata_usia'},inplace=True)


###########3 dataframe persentase pria & wanita tiap profesi

persentase = pd.crosstab(a.occupation, a.gender).apply(lambda r: r/r.sum(), axis=1) * 100
persentase['%total'] = persentase['F']+persentase['M']
persentase.rename(columns={'F':'%female','M':'%male'},inplace=True)
persentase = persentase[['%male','%female','%total']]
persentase