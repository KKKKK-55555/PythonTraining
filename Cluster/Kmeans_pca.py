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

# K-means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)
pred_class = kmeans.predict(X)

# PCA
pca = PCA(n_components=2) # transform into 2d
pca_X = pca.fit_transform(X)

# Plot scatter graph
fig, axs = plt.subplots(1, 2)

axs[0].scatter(pca_X[:,0], pca_X[:,1], c=pred_class, cmap='viridis')
axs[1].scatter(pca_X[:,0], pca_X[:,1], c=y, cmap='viridis')

for i in range(2):
    axs[i].set_xlabel('PCA Component 1')
    axs[i].set_ylabel('PCA Component 2')
#plt.colorbar(label='Class')
#plt.savefig('fig_KmeansPCA.png')
plt.show()
