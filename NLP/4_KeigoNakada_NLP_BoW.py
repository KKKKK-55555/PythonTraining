from sklearn.feature_extraction.text import CountVectorizer

"""
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
"""

corpus = ["Natural language processing is fascinating."]

if __name__ == '__main__':
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names_out())
    print(X.toarray())