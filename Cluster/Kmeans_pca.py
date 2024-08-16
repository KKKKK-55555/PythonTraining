import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
print(f"X.shape{X.shape}")

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# PCA
pca = PCA(n_components=2) # transform into 2d
X_pca = pca.fit_transform(X)
print(f"X_pca.shape({X_pca.shape})")

# Plot scatter graph
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.colorbar(scatter, label='Cluster Level')
plt.xlabel('PCA Component 1')
plt.xlabel('PCA Component 2')
plt.savefig('fig_Kmeans2PCA.png')
plt.show()
