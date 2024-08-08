from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


# サンプルデータ
texts = [
    "I love this movie",
    "This movie is awful",
    "Great acting",
    "Terrible plot",
    "Highly recommended"
]

labels = [1, 0, 1, 0, 1] # 1: positive, 0: negative

# 特徴量抽出
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# データ分割
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42)

# モデルの学習
clf = MultinomialNB()
clf.fit(X_train, y_train)

# 予測
y_pred = clf.predict(X_test)
print("Predictions:", y_pred)
