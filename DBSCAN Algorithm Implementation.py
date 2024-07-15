import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Dataset: Points
points = np.array([(1, 2), (1.5, 1.8), (5, 8), (8, 8), (1, 0.6), (9, 11)])

# DBSCAN parameters
epsilon = 2.0
min_samples = 2

# Initialize and fit DBSCAN
dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
dbscan.fit(points)

# Get the cluster labels
labels = dbscan.labels_

# Print the points with their respective cluster labels
for point, label in zip(points, labels):
    print(f"Point {point} is in cluster {label}")

# Plotting the points and clusters
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = points[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

plt.title('DBSCAN Clustering')
plt.show()
