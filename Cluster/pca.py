import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


# データセットの読み込み
iris = load_iris()
X = iris.data
y = iris.target

# PCAの実行
pca = PCA(n_components=2) # 2次元に変換
X_pca = pca.fit_transform(X)

# 主成分の分散説明率を表示
print('Explained variance ratio:', pca.explained_variance_ratio_)

# データの可視化
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.colorbar(label='Class')
plt.show()
