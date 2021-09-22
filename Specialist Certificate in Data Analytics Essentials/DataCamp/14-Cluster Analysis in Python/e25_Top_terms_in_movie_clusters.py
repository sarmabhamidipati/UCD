"""
Top terms in movie clusters
Now that you have created a sparse matrix, generate cluster centers and print the top three terms in each cluster.
Use the .todense() method to convert the sparse matrix, tfidf_matrix to a normal matrix for the kmeans() function
to process. Then, use the .get_feature_names() method to get a list of terms in the tfidf_vectorizer object.
The zip() function in Python joins two lists.

The tfidf_vectorizer object and sparse matrix, tfidf_matrix, from the previous have been retained in this exercise.
kmeans has been imported from SciPy.

With a higher number of data points, the clusters formed would be defined more clearly. However, this requires
some computational power, making it difficult to accomplish in an exercise here.
"""
from nltk.tokenize import word_tokenize
import re
# Import TfidfVectorizer class from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq


def remove_noise(text, stop_words = []):
    tokens = word_tokenize(text)
    cleaned_tokens = []
    for token in tokens:
        token = re.sub('[^A-Za-z0-9]+', '', token)
        if len(token) > 1 and token.lower() not in stop_words:
            # Get lowercase
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=1.0, max_features=50, min_df=0.0, tokenizer=remove_noise)

plots = \
    ['Cable Hogue is isolated in the desert, awaiting his partners, Taggart and Bowen, who are scouting for water. '
     'The two plot to seize what little water remains to save themselves. Cable, who hesitates to defend himself, '
     'is disarmed and abandoned to almost certain death.\r\nConfronted with sandstorms and other desert elements, '
     'Cable bargains with God. Four days later, about to perish, he stumbles upon a muddy pit. He digs and discovers '
     'an abundant supply of water.\r\nAfter discovering that his well is the only source of water between two towns '
     'on a stagecoach route, he decides to live there and build a business. Cable\'s first paying customer is the '
     'Rev. Joshua Duncan Sloane, a wandering minister of a church of his own revelation. Joshua doubts the legitimacy '
     'of Cable\'s claim to the spring, prompting Cable to race into town to file at the land office.\r\nCable faces '
     'the mockery of everyone he tells about his discovery. That does not deter him from buying 2 acres (0.8\xa0ha) '
     'surrounding his spring. He immediately goes to the stage office to drum up business but is thrown out by the '
     'skeptical owner. He pitches his business plan to a bank president, who is dubious about the claim. Cable ']

# Use the .fit_transform() method on the list plots
tfidf_matrix = tfidf_vectorizer.fit_transform(plots)

num_clusters = 2

# Generate cluster centers through the kmeans function
cluster_centers, distortion = kmeans(tfidf_matrix.todense(), num_clusters)

# Generate terms from the tfidf_vectorizer object
terms = tfidf_vectorizer.get_feature_names()

for i in range(num_clusters):
    # Sort the terms and print top 3 terms
    center_terms = dict(zip(terms, list(cluster_centers[i])))
    sorted_terms = sorted(center_terms, key=center_terms.get, reverse=True)
    print(sorted_terms[:3])