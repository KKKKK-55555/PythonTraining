import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# Load dataset
iris = load_iris()
X = iris.data
print(f"X.shape{X.shape}")

# K-means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Plot scatter graph
pred_class = kmeans.predict(X)

plt.scatter(X[pred_class == 0, 0], X[pred_class == 0, 1],
            c='red', label='cluster 0')
plt.scatter(X[pred_class == 1, 0], X[pred_class == 1, 1],
            c='blue', label='cluster 1')
plt.scatter(X[pred_class == 2, 0], X[pred_class == 2, 1],
            c='green', label='cluster 2')

plt.scatter(kmeans.cluster_centers_[:, 1],
            kmeans.cluster_centers_[:, 1],
            s=250, marker='*',
            c='black',
            label='center')

plt.legend()
plt.show()
