"""
NMF features of the Wikipedia articles

"""
import numpy as np
from sklearn.decomposition import NMF
import pandas as pd

articles = np.array([[0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.]])

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

titles = ['HTTP 404',
          'Alexa Internet',
          'Internet Explorer',
          'HTTP cookie',
          'Google Search',
          'Tumblr',
          'Hypertext Transfer Protocol',
          'Social search',
          'Firefox',
          'LinkedIn',
          'Global warming',
          'Nationally Appropriate Mitigation Action',
          'Nigel Lawson',
          'Connie Hedegaard',
          'Climate change',
          'Kyoto Protocol',
          '350.org',
          'Greenhouse gas emissions by the United States',
          '2010 United Nations Climate Change Conference',
          '2007 United Nations Climate Change Conference',
          'Angelina Jolie',
          'Michael Fassbender',
          'Denzel Washington',
          'Catherine Zeta-Jones',
          'Jessica Biel',
          'Russell Crowe',
          'Mila Kunis',
          'Dakota Fanning',
          'Anne Hathaway',
          'Jennifer Aniston',
          'France national football team',
          'Cristiano Ronaldo',
          'Arsenal F.C.',
          'Radamel Falcao',
          'Zlatan Ibrahimović',
          'Colombia national football team',
          '2014 FIFA World Cup qualification',
          'Football',
          'Neymar',
          'Franck Ribéry',
          'Tonsillitis',
          'Hepatitis B',
          'Doxycycline',
          'Leukemia',
          'Gout',
          'Hepatitis C',
          'Prednisone',
          'Fever',
          'Gabapentin',
          'Lymphoma',
          'Chad Kroeger',
          'Nate Ruess',
          'The Wanted',
          'Stevie Nicks',
          'Arctic Monkeys',
          'Black Sabbath',
          'Skrillex',
          'Red Hot Chili Peppers',
          'Sepsis',
          'Adam Levine']


# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features,index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])