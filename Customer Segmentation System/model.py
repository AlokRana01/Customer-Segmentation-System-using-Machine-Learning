import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pickle

# Load dataset
data = pd.read_csv('Mall_Customers.csv')

# Select features
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# -------------------------------
# ELBOW METHOD (for best K)
# -------------------------------
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# -------------------------------
# FINAL MODEL (K = 5)
# -------------------------------
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# -------------------------------
# VISUALIZATION
# -------------------------------
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=kmeans.labels_)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.show()

# Save model
pickle.dump(kmeans, open('model.pkl', 'wb'))

print("Model trained and saved successfully!")