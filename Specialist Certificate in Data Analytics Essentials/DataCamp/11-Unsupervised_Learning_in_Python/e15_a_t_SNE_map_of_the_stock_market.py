"""
A t-SNE map of the stock market
 The stock price movements for each company are available as the array normalized_movements
 (these have already been normalized for you). The list companies gives the name of each company.
 PyPlot (plt) has been imported for you.
 Instructions
100 XP

    Import TSNE from sklearn.manifold.
    Create a TSNE instance called model with learning_rate=50.
    Apply the .fit_transform() method of model to normalized_movements. Assign the result to tsne_features.
    Select column 0 and column 1 of tsne_features.
    Make a scatter plot of the t-SNE features xs and ys. Specify the additional keyword argument alpha=0.5.
    Code to label each point with its company name has been written for you using plt.annotate(),
    so just hit 'Submit Answer' to see the visualization!

"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

normalized_movements = np.array([
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.01796837, 0.00112314, 0., -0.00673829, 0.02919855, 0.01123007],
    [0.00302051, -0.00114574, -0.01775851, -0.02791349, 0.00437463, -0.10202026],
    [-0.02599391, -0.02639998, -0.00852927, -0.00162466, -0.01624623, 0.02680614],
    [-0.02208986, 0.01184398, -0.02208986, 0.04502568, -0.01654394, 0.03515588],
    [0.01981027, 0.01059598, 0.02626006, -0.01197837, 0.01842816, 0.02211388],
    [0.0200991, 0.00223323, -0.01786587, -0.0066997, 0.00446647, -0.0066997]
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
# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:, 0]

# Select the 1th feature: ys
ys = tsne_features[:, 1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()