# Importing necessary libraries
import math

# Define the dataset
points = [(1, 2), (1.5, 1.8), (5, 8), (8, 8), (1, 0.6), (9, 11)]

# Number of clusters (K)
K = 2

# Initialize centroids (randomly chosen from points)
centroid1 = (1, 2)
centroid2 = (5, 8)

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to assign points to clusters
def assign_clusters(points, centroid1, centroid2):
    cluster1 = []
    cluster2 = []
    
    for point in points:
        dist_to_c1 = euclidean_distance(point, centroid1)
        dist_to_c2 = euclidean_distance(point, centroid2)
        
        if dist_to_c1 < dist_to_c2:
            cluster1.append(point)
        else:
            cluster2.append(point)
    
    return cluster1, cluster2

# Function to update centroids
def update_centroids(cluster1, cluster2):
    centroid1 = (sum([point[0] for point in cluster1]) / len(cluster1),
                 sum([point[1] for point in cluster1]) / len(cluster1))
    
    centroid2 = (sum([point[0] for point in cluster2]) / len(cluster2),
                 sum([point[1] for point in cluster2]) / len(cluster2))
    
    return centroid1, centroid2

# Print initial centroids
print("Initial Centroids:")
print("Centroid 1:", centroid1)
print("Centroid 2:", centroid2)
print()

# Step-by-step K-Means process
for iteration in range(1, 4):  # Perform 3 iterations (you can adjust as needed)
    print(f"Iteration {iteration}:")
    
    # Assign points to clusters
    cluster1, cluster2 = assign_clusters(points, centroid1, centroid2)
    print("Cluster 1:", cluster1)
    print("Cluster 2:", cluster2)
    
    # Update centroids
    centroid1, centroid2 = update_centroids(cluster1, cluster2)
    print("Updated Centroid 1:", centroid1)
    print("Updated Centroid 2:", centroid2)
    print("--------------------------------------------------")
    
    # Check for convergence (in a real implementation, you'd use a convergence criterion)
    # For simplicity, we're just printing the intermediate steps here
    
# Final clusters and centroids after iterations
print("Final Clusters:")
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Final Centroids:")
print("Centroid 1:", centroid1)
print("Centroid 2:", centroid2)
print()
print("=== Code Execution Successful ===")
