"""
in the NSFG dataset, the variable 'outcome' encodes the outcome of each pregnancy as shown below:
The nsfg DataFrame has been pre-loaded for you. Explore it in the IPython Shell and
use the methods Allen showed you in the video to
answer the following question: How many pregnancies in this dataset ended with a live birth?

value 	label
1 	Live birth
2 	Induced abortion
3 	Stillbirth
4 	Miscarriage
5 	Ectopic pregnancy
6 	Current pregnancy

Possible Answers

    6489
    9538
    1469
    6
"""
import pandas as pd

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')

print(nsfg['outcome'].value_counts())

print(nsfg[nsfg['outcome'] == 1].count())
