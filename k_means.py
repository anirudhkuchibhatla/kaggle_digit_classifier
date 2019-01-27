import pandas as pd
from sklearn.cluster import KMeans

test_data = pd.read_csv("test.csv")

kmeans = KMeans(n_clusters=10).fit(test_data)

predictions = [(i*2 +2) for i in kmeans.labels_]

