import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# PCA
pca = PCA(n_components=2) # 2次元に変換
X_pca = pca.fit_transform(X)

# Print principle R^2
print('Explained variance ratio:', pca.explained_variance_ratio_)

# Plot scatter graph
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.colorbar(label='Class')

plt.show()
