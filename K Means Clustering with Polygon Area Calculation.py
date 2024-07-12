import numpy as np
from math import tan, pi, sqrt

# K-means Clustering Algorithm
def kmeans(points, k, max_iterations=100):
    # Randomly choose initial centroids
    centroids = points[np.random.choice(points.shape[0], k, replace=False)]
    
    for _ in range(max_iterations):
        # Assign points to the nearest centroid
        distances = np.sqrt(((points - centroids[:, np.newaxis])**2).sum(axis=2))
        closest_centroids = np.argmin(distances, axis=0)
        
        # Calculate new centroids
        new_centroids = np.array([points[closest_centroids == i].mean(axis=0) for i in range(k)])
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return centroids, closest_centroids

# Polygon Area Calculation Functions
def calculate_apothem(side_length, num_sides):
    return side_length / (2 * tan(pi / num_sides))

def calculate_polygon_area(side_length, num_sides):
    apothem = calculate_apothem(side_length, num_sides)
    perimeter = num_sides * side_length
    area = (1/2) * perimeter * apothem
    return area

def calculate_polygon_area_direct(side_length, num_sides):
    return (num_sides * side_length**2) / (4 * tan(pi / num_sides))

# Example usage
if __name__ == "__main__":
    # Example points
    points = np.array([
        [1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]
    ])

    # Perform K-means clustering
    k = 2
    centroids, clusters = kmeans(points, k)

    print("Centroids:", centroids)
    print("Cluster assignments:", clusters)

    # Example for polygon area calculation
    side_length = 5
    num_sides = 6  # Example for a hexagon

    apothem = calculate_apothem(side_length, num_sides)
    area = calculate_polygon_area(side_length, num_sides)
    direct_area = calculate_polygon_area_direct(side_length, num_sides)

    print(f"Apothem of the polygon: {apothem}")
    print(f"Area of the polygon (using perimeter and apothem): {area}")
    print(f"Area of the polygon (using direct formula): {direct_area}")
