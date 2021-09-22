"""
TF-IDF of movie plots
Let us use the plots of randomly selected movies to perform document clustering on.
Before performing clustering on documents, they need to be cleaned of any unwanted noise
(such as special characters and stop words) and converted into a sparse matrix through TF-IDF of the documents.

Use the TfidfVectorizer class to perform the TF-IDF of movie plots stored in the list plots.
The remove_noise() function is available to use as a tokenizer in the TfidfVectorizer class.
The .fit_transform() method fits the data into the TfidfVectorizer objects and then generates the TF-IDF sparse matrix.

Note: It takes a few seconds to run the .fit_transform() method.

    Import TfidfVectorizer class from sklearn.
    Initialize the TfidfVectorizer class with minimum and maximum frequencies of 0.1 and 0.75, and 50 maximum features.
    Use the fit_transform() method on the initialized TfidfVectorizer class with the list plots.

"""
from nltk.tokenize import word_tokenize
import re
# Import TfidfVectorizer class from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer


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
