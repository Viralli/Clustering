import numpy as np
from sklearn.cluster import DBSCAN

# Sample data points
X = np.array([[1, 2], [1, 1], [1.5, 1.8], [0, 1], [1, 0.6], [5, 8], [8, 8], [9, 11]])

# DBSCAN parameters
eps = 2.0
min_pts = 2

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=eps, min_samples=min_pts)
labels = dbscan.fit_predict(X)

# Retrieve core samples and labels
core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True

# Print DBSCAN parameters and explanations
print("DBSCAN Parameters and Explanations:")
print(f"eps: {eps} (maximum radius of the neighborhood)")
print(f"min_pts: {min_pts} (minimum number of points to form a cluster)\n")

# Print DBSCAN clustering results
print("DBSCAN Clustering Results:")
for i in range(len(X)):
    if core_samples_mask[i]:
        print(f"Choosing Core Point: {X[i]}")
        neighbors = np.where(dbscan.components_ == i)[0]
        print(f"Finding Eps-Neighborhood: {list(neighbors)}")
        print(f"Core Point Check: Point {X[i]} is chosen as a core point with neighbors {list(neighbors)}.")

        # Handling noise
        if labels[i] == -1:
            print("Handling Noise: This core point has been marked as noise.")
        else:
            print(f"Expand the Cluster: Expanding cluster around point {X[i]} with neighbors {list(neighbors)}.")
            print(f"Assign Border Points: Assigning border points to cluster {labels[i]}.\n")

# Print noise points
print("Noise Points:")
for i in range(len(X)):
    if labels[i] == -1:
        print(f"Noise Identification: Point {X[i]}.")

# Print final clusters
print("\nFinal Clusters:")
unique_labels = set(labels)
for label in unique_labels:
    if label != -1:
        print(f"\nCluster {label}: Points {list(X[labels == label])}")
