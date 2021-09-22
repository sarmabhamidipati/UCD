"""
Hierarchies of stocks
linkage and dendrogram have already been imported from scipy.cluster.hierarchy, and PyPlot has been imported as plt.
Instructions
100 XP

    Import normalize from sklearn.preprocessing.
    Rescale the price movements for each stock by using the normalize() function on movements.
    Apply the linkage() function to normalized_movements, using 'complete' linkage,
    to calculate the hierarchical clustering. Assign the result to mergings.
    Plot a dendrogram of the hierarchical clustering, using the list companies of company names as the labels.
    In addition, specify the leaf_rotation=90, and leaf_font_size=6 keyword arguments
    as you did in the previous exercise.

"""
import np as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import normalize

movements = np.array(
    [
[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
[-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
[-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
[-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
[-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
[4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
[4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
[-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
[9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
[-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
[1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
[-6.0001000e-02, 2.5999800e-01, 9.9998000e-02],
[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
[-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
[-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
[-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
[-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
[4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
[4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
[-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
[9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
[-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
[1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
[-6.0001000e-02, 2.5999800e-01, 9.9998000e-02],
[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
[-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
[-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
[-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
[-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
[4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
[4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
[-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
[9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
[-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
[1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
[-6.0001000e-02, 2.5999800e-01, 9.9998000e-02],
[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
[-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
[-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
[-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
[-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
[4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
[4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
[-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
[9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
[-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
[1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
[-6.0001000e-02, 2.5999800e-01, 9.9998000e-02],
[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
[-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
[-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
[-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
[-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
[4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
[4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
[-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
[9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
[-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
[1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
[-6.0001000e-02, 2.5999800e-01, 9.9998000e-02]
     ]
)

companies = ['Apple',
             'AIG',
             'Amazon',
             'American express',
             'Boeing',
             'Bank of America',
             'British American Tobacco',
             'Canon',
             'Caterpillar',
             'Colgate-Palmolive',
             'ConocoPhillips',
             'Cisco',
             'Chevron',
             'DuPont de Nemours',
             'Dell',
             'Ford',
             'General Electrics',
             'Google/Alphabet',
             'Goldman Sachs',
             'GlaxoSmithKline',
             'Home Depot',
             'Honda',
             'HP',
             'IBM',
             'Intel',
             'Johnson & Johnson',
             'JPMorgan Chase',
             'Kimberly-Clark',
             'Coca Cola',
             'Lookheed Martin',
             'MasterCard',
             'McDonalds',
             '3M',
             'Microsoft',
             'Mitsubishi',
             'Navistar',
             'Northrop Grumman',
             'Novartis',
             'Pepsi',
             'Pfizer',
             'Procter Gamble',
             'Philip Morris',
             'Royal Dutch Shell',
             'SAP',
             'Schlumberger',
             'Sony',
             'Sanofi-Aventis',
             'Symantec',
             'Toyota',
             'Total',
             'Taiwan Semiconductor Manufacturing',
             'Texas instruments',
             'Unilever',
             'Valero Energy',
             'Walgreen',
             'Wells Fargo',
             'Wal-Mart',
             'Exxon',
             'Xerox',
             'Yahoo']
# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method='complete')

# Plot the dendrogram
dendrogram(mergings,
           labels=companies,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()
