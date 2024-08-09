from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# データのロード
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train',
                                  categories=categories,
                                  shuffle=True,
                                  random_state=42)

twenty_test = fetch_20newsgroups(subset='test',
                                 categories=categories,
                                 shuffle=True,
                                 random_state=42)

# 特徴量抽出
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(twenty_train.data)
print(X_train_counts.shape)

tf_vectorizer = TfidfVectorizer()
X_train_tfid = tf_vectorizer.fit_transform(twenty_train.data)

# transform
tf_transformer = TfidfTransformer()
X_train_tf = tf_transformer.fit_transform(X_train_counts)

# train
clf_NB = MultinomialNB()
clf_NB.fit(X_train_tf, twenty_train.target)

# predict
X_test_counts = vectorizer.transform(twenty_test.data)
X_test_tf = tf_transformer.fit_transform(X_test_counts)
print(X_test_counts.shape)

y_pred = clf_NB.predict(X_test_tf)
print(f"{f1_score(twenty_test.target, y_pred, average='weighted')}")

# LR
clf_LR = LogisticRegression()
clf_LR.fit(X_train_tfid, twenty_train.target)

# predict
X_test_tfid = tf_vectorizer.transform(twenty_test.data)
y_pred = clf_LR.predict(X_test_tfid)
y_prob = clf_LR.predict_proba(X_test_tfid)

print(f"{f1_score(twenty_test.target, y_pred, average='weighted')}")
