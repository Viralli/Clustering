import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# Generate synthetic dataset
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
print("Dataset with clear cluster structure generated.")

# Function to plot clusters
def plot_clusters(X, y_pred, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()

# Flat Algorithm: KMeans (Hard Clustering)
print("\nApplying Flat Algorithm: KMeans (Hard Clustering)")
kmeans = KMeans(n_clusters=4)
y_kmeans = kmeans.fit_predict(X)
plot_clusters(X, y_kmeans, "KMeans Clustering (Hard Clustering)")

# Hierarchical Algorithm: Agglomerative Clustering (Hard Clustering)
print("\nApplying Hierarchical Algorithm: Agglomerative Clustering (Hard Clustering)")
agg_clustering = AgglomerativeClustering(n_clusters=4)
y_agg = agg_clustering.fit_predict(X)
plot_clusters(X, y_agg, "Agglomerative Clustering (Hard Clustering)")

# Soft Clustering: Gaussian Mixture Model (GMM)
print("\nApplying Soft Clustering: Gaussian Mixture Model (GMM)")
gmm = GaussianMixture(n_components=4)
y_gmm = gmm.fit_predict(X)
plot_clusters(X, y_gmm, "Gaussian Mixture Model (Soft Clustering)")

# GMM also provides the probability of each sample belonging to each cluster
y_gmm_proba = gmm.predict_proba(X)
print("\nSample cluster probabilities (first 5 samples):")
print(y_gmm_proba[:5])
