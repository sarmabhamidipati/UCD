"""
Clustering Wikipedia part II
It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf
word-frequencies of some popular Wikipedia articles, and a list titles of their titles.
Use your pipeline to cluster the Wikipedia articles.

A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline
chaining TruncatedSVD with KMeans is available.
"""
import numpy as np
# Import pandas
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline


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
               [0., 0., 0., 0., 0., 0.]
               ])


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

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=5)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values(by='label'))
