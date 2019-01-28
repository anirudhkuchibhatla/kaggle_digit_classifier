import pandas as pd
from sklearn.cluster import KMeans

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

trained_rows = pd.DataFrame(columns=test_data.columns)
labels = []
while len(labels) < 10:
    for index, row in train_data.iterrows():
        if row['label'] not in labels:
            labels.append(row['label'])
            trained_rows = trained_rows.append(row)
            print(row)

print(labels)
print(trained_rows)
#kmeans = KMeans(n_clusters=10).fit(test_data)

#predictions = kmeans.labels



