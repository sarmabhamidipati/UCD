import pandas as pd
import numpy as np


nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')
print(nsfg.shape)

# print(nsfg.columns)

# for i, r in nsfg.iterows():
#    print(i, r)

pd.options.display.max_columns = None
# print(nsfg.tail())

# print(nsfg["birthwgt_lb1"].head())

pounds = nsfg['birthwgt_lb1']
# print(type(pounds))
# print(pounds.value_counts().sort_index())

# print(pounds.describe())

# print(nsfg.info())

# print("Total rows where birthwgt_lb1 data not found ")
# print(nsfg["birthwgt_lb1"].isna().sum())
# print("Total rows where birthwgt_lb1 data found ")
# print(nsfg["birthwgt_lb1"].notna().sum())

# print("Max Value:",nsfg["birthwgt_lb1"].max(), "Min Value:", nsfg["birthwgt_lb1"].min())

print(nsfg)
print(nsfg["birthwgt_lb1"].value_counts(ascending=True).sort_index())

# get all rows where nith weight in lbl is 0.0
print(nsfg[nsfg["birthwgt_lb1"] == 0.0])

# get all rows where nith weight in lbl is NaN
print(nsfg[nsfg["birthwgt_lb1"].isna()])
