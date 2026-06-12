# Deeper into Unsupervised Learning

In unsupervised learning, you take away the labels. The algorithm only gets the input features ($X$) and has to figure out the structure of the data completely on its own.

Unsupervised learning is highly valuable for discovery and data preparation, falling mostly into two categories:

---

## A. Clustering (Finding Groups)

The algorithm looks for data points that are mathematically close to each other and groups them together.

* **How it works:** In algorithms like K-Means, you tell the model how many groups ($K$) you want. It drops $K$ random center points (centroids) into your data, measures the distance from every data point to those centers, and shifts the centers until it finds the most logical groupings.
* **Use Cases:** Customer segmentation, identifying abnormal network traffic.

---

## B. Dimensionality Reduction (Simplifying Data)

Sometimes you have too much data (e.g., 500 different features for a single item). Dimensionality reduction compresses the data while keeping the most important information intact.

* **How it works:** Algorithms like **Principal Component Analysis (PCA)** mathematically squash the data down to its most crucial variables, making it easier to visualize and faster to process in other machine learning models.
