import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

gss = pd.read_hdf('gss.hdf5', 'gss')
print(gss.head())

educ = gss['educ']
#print(educ)
plt.xlabel("Years of Education")
plt.ylabel("Count")

plt.hist(educ.dropna(), label="educ")
plt.show()

#pmf_educ = Pmf(educ, normalize=False)
#pmf_educ.head()