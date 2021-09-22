"""
Recommend musical artists part II
A solution to the previous exercise has been run, so norm_features is an array containing the
normalized NMF features as rows. The names of the musical artists are available as the list artist_names.

Instructions
100 XP

    Import pandas as pd.
    Create a DataFrame df from norm_features, using artist_names as an index.
    Use the .loc[] accessor of df to select the row of 'Bruce Springsteen'. Assign the result to artist.
    Apply the .dot() method of df to artist to calculate the dot product of every row with artist.
    Save the result as similarities.
    Print the result of the .nlargest() method of similarities to display
    the artists most similar to 'Bruce Springsteen'.

"""
import numpy as np
# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline
import pandas as pd

artists = np.array([[0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.]])

artist_names = ['Massive Attack',
                'Sublime',
                'Beastie Boys',
                'Neil Young',
                'Dead Kennedys',
                'Orbital',
                'Miles Davis',
                'Leonard Cohen',
                'Van Morrison',
                'NOFX',
                'Rancid',
                'Lamb',
                'Korn',
                'Dropkick Murphys',
                'Bob Dylan',
                'Eminem',
                'Nirvana',
                'Van Halen',
                'Damien Rice',
                'Elvis Costello',
                'Everclear',
                'Jimi Hendrix',
                'PJ Harvey',
                'Red Hot Chili Peppers',
                'Ryan Adams',
                'Soundgarden',
                'The White Stripes',
                'Madonna',
                'Eric Clapton',
                'Bob Marley',
                'Dr. Dre',
                'The Flaming Lips',
                'Tom Waits',
                'Moby',
                'Cypress Hill',
                'Garbage',
                'Fear Factory',
                '50 Cent',
                'Ani DiFranco',
                'Matchbox Twenty',
                'The Police',
                'Eagles',
                'Phish',
                'Stone Temple Pilots',
                'Black Sabbath',
                'Britney Spears',
                'Fatboy Slim',
                'System of a Down',
                'Simon & Garfunkel',
                'Snoop Dogg',
                'Aimee Mann',
                'Less Than Jake',
                'Rammstein',
                'Reel Big Fish',
                'The Prodigy',
                'Pantera',
                'Foo Fighters',
                'The Beatles',
                'Incubus',
                'Audioslave',
                'Bright Eyes',
                'Machine Head',
                'AC/DC',
                'Dire Straits',
                'MotÃ¶rhead',
                'Ramones',
                'Slipknot',
                'Me First and the Gimme Gimmes',
                'Bruce Springsteen',
                'Queens of the Stone Age',
                'The Chemical Brothers',
                'Bon Jovi',
                'Goo Goo Dolls',
                'Alice in Chains',
                'Howard Shore',
                'Barenaked Ladies',
                'Anti-Flag',
                'Nick Cave and the Bad Seeds',
                'Static-X',
                'Misfits',
                '2Pac',
                'Sparta',
                'Interpol',
                'The Crystal Method',
                'The Beach Boys',
                'Goldfrapp',
                'Bob Marley & the Wailers',
                'Kylie Minogue',
                'The Blood Brothers',
                'Mirah',
                'Ludacris',
                'Snow Patrol',
                'The Mars Volta',
                'Yeah Yeah Yeahs',
                'Iced Earth',
                'Fiona Apple',
                'Rilo Kiley',
                'Rufus Wainwright',
                'Flogging Molly',
                'Hot Hot Heat',
                'Dredg',
                'Switchfoot',
                'Tegan and Sara',
                'Rage Against the Machine',
                'Keane',
                'Jet',
                'Franz Ferdinand',
                'The Postal Service',
                'The Dresden Dolls',
                'The Killers',
                'Death From Above 1979']

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
