from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np


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

# 
tf_transformer = TfidfTransformer()
X_train_tf = tf_transformer.fit_transform(X_train_counts)

# モデルの学習
clf = MultinomialNB()
clf.fit(X_train_tf, twenty_train.target)

# 予測
X_test_counts = vectorizer.transform(twenty_test.data)
X_test_tf = tf_transformer.fit_transform(X_test_counts)

print(X_test_counts.shape)
y_pred = clf.predict(X_test_tf)
print(f'{np.mean(y_pred == twenty_test.target)}')
