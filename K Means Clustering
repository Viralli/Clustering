from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# K-Means Clustering
kmeans = KMeans(n_clusters=4)
kmeans_labels = kmeans.fit_predict(X)

# Function to plot clusters
def plot_clusters(X, labels, title):
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6, edgecolors='w')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Plotting clustered data points
plot_clusters(X, kmeans_labels, "K-Means Clustering")

# Function to plot convex hulls
def plot_convex_hulls(X, labels):
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:
            continue
        points = X[labels == label]
        hull = ConvexHull(points)
        plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], alpha=0.2, label=f'Cluster {label+1} Convex Hull')

    plt.title('Convex Hulls of Clusters')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# Plotting convex hulls of clusters
plot_convex_hulls(X, kmeans_labels)
