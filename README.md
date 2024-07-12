# Clustering Algorithms Project

  # Overview

        This project demonstrates various clustering algorithms and techniques for visualizing clusters. The focus is on DBSCAN and K-Means clustering methods, along with a polygon function to visualize cluster boundaries. Detailed explanations of respective clusterings 
        are mentioned in their respective files.

  # What is Clustering?

        Clustering is a technique used in data analysis and machine learning to group a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups. It helps in identifying patterns and 
        structures in data, making it a fundamental tool in exploratory data analysis.

  # What is DBSCAN Clustering?

        DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that groups points based on the density of data points in the dataset. Unlike other clustering algorithms, DBSCAN can identify clusters of varying shapes and sizes, and 
        it is particularly effective in detecting outliers (noise).

        Detailed explanations and examples of DBSCAN clustering can be found in the `DBSCAN_Clustering.md` file.

  # Why Do We Need DBSCAN Clustering?

        DBSCAN is advantageous in scenarios where:

        1. The data contains clusters of varying shapes and sizes.
        2. There is a significant presence of noise or outliers.
        3. Predefining the number of clusters is not feasible.

  # Polygon Function in Clustering

        The polygon function helps visualize the boundaries of clusters.
        Detailed explanations and examples of the polygon function in clustering can be found in the `Polygon_Function_Clustering.md` file.

  # K-Means Clustering

       K-Means is a clustering algorithm that partitions the dataset into a predefined number of clusters (k). It aims to minimize the variance within each cluster. The algorithm works by iteratively updating the cluster centroids until convergence.

  # Outputs

  1. Basic DBSCAN Clustering (DBSCAN clustering for first set of points(Part -1)):

        ![dbscan_eps_min_sample_data_1 py - Part 1](https://github.com/Viralli/Clustering/assets/92823324/4b378bcf-eb5b-4369-a710-3b513e226578)

  2. Basic DBSCAN Clustering (DBSCAN clustering for first set of points(Part -2)):

        ![dbscan_eps_min_sample_data_1 py - Part 2](https://github.com/Viralli/Clustering/assets/92823324/08a54178-3c6a-4013-8a5c-dc7d1f721d1a)

  3. Modified DBSCAN Clustering (DBSCAN clustering for Second set of points(Part -1)):

        ![dbscan_eps_min_sample_data_2 py - Part 1](https://github.com/Viralli/Clustering/assets/92823324/84140b5c-e120-4909-b3d6-710a9884ff58)

  4. Modified DBSCAN Clustering (DBSCAN clustering for Second set of points(Part -2)):

        ![dbscan_eps_min_sample_data_2 py - Part 2](https://github.com/Viralli/Clustering/assets/92823324/00681472-8545-4df3-a95e-62eff0be282a)

  5. K Means Clustering(Part -1):

        ![K Means Clustering - Output Part 1](https://github.com/Viralli/Clustering/assets/92823324/22b61e69-419b-4cb8-9703-fde0c366d279)

  6. K Means Clustering(Part -2):
    
        ![K Means Clustering - Output Part 2](https://github.com/Viralli/Clustering/assets/92823324/2086356e-1b57-4d5c-b084-54a1eabed024)

  7. K Means Clustering (Convex hull of Clusters) Part - 1:

        ![K Means Clustering (Convex Hulls of Clusters) - Output Part 1](https://github.com/Viralli/Clustering/assets/92823324/cfafa7f3-5769-4621-ae35-6bdbb426c01b)

  8.  K Means Clustering (Convex hull of Clusters) Part - 2:

         ![K Means Clustering (Convex Hulls of Clusters) - Output Part 2](https://github.com/Viralli/Clustering/assets/92823324/ec3eb828-8771-402e-8bda-2b7a368e10f2)

  9. K Means Clustering with Polygon Area Calculation - Part 1:

      ![K Means Clustering with Polygon Area Calculation - Part 1](https://github.com/user-attachments/assets/c36e3b78-1925-4349-aab5-e2cc38d08f33)

 10. K Means Clustering with Polygon Area Calculation - Part 2:

      ![K Means Clustering with Polygon Area Calculation - Part 2](https://github.com/user-attachments/assets/d251a3c8-4e54-4652-9de7-9f53bd608f4b)

  # Conclusion

  This project provides an overview of different clustering techniques and demonstrates their implementation using Python. By visualizing clusters and their boundaries, it becomes easier to understand the structure and patterns within the data.   
