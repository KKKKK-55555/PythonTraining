import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster


# データセットの読み込み
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("df.head():¥n", df.head())

# 階層クラスタリングの実行（ウォード法）
Z = linkage(df, method='ward')

# デンドログラムのプロット
plt.figure(figsize=(10, 7))
dendrogram(Z, truncate_mode='level', p=3)
plt.title('Hierarchical Clustering Dendrogram (Ward’s Method)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
#plt.show()

fig, axs = plt.subplots(3, 3, figsize=(16, 12))
max_d = 0

for i in range(3):
    for j in range(3):
        # クラスタの切り出し
        max_d += 1 # これはデンドログラムの距離に基づいて決定
        clusters = fcluster(Z, max_d, criterion='distance')

        # クラスタ結果の可視化（便宜的に2つの次元を選択）
        df['cluster'] = clusters
        axs[i][j].scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['cluster'], cmap='viridis')
        axs[i][j].set_title(f"max_d={max_d}, n_cluster={len(df['cluster'].unique())}")

#plt.xlabel(iris.feature_names[0])
#plt.ylabel(iris.feature_names[1])
#plt.title('Hierarchical Clustering (Ward’s Method)')
plt.tight_layout()
plt.show()