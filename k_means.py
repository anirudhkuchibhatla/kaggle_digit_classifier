import pandas as pd
from sklearn.cluster import KMeans

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

#Sets final rows as empty data fram with same columns as test_data
#Used to help mark test data
final_rows = pd.DataFrame(columns=test_data.columns)
labels = []
while len(labels) < 10:
    for index, row in train_data.iterrows():
        if row['label'] not in labels:
            labels.append(row['label'])
            final_rows = final_rows.append(row)
            print(row)

print(labels)
print(final_rows)
test_marker = final_rows.drop('label', 1)
final_test = test_data.append(final_rows)

#Run the K-means clustering algorithm to classify digits.
kmeans = KMeans(n_clusters=10).fit(final_test)


predictions = kmeans.labels

marked_predictions = predictions[-10:]

match_dict = {}
#Rematches labels to correct number
for i in range(10):
    break



