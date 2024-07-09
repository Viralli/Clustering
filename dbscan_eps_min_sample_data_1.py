from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=10)
dbscan_labels = dbscan.fit_predict(X)

# Plotting results
def plot_clusters(X, labels, title):
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title(title)
    plt.show()

def plot_polygon(X, labels):
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:
            continue
        points = X[labels == label]
        hull = ConvexHull(points)
        plt.plot(points[:, 0], points[:, 1], 'o')
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    plt.show()

plot_clusters(X, dbscan_labels, "DBSCAN Clustering")
plot_polygon(X, dbscan_labels)
