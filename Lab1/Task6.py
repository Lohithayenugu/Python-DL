import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="white", color_codes=True)
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
train = pd.read_csv('./diamonds.csv')
categorical_data = train.select_dtypes(exclude=[np.number])
categorical_features = list(categorical_data.columns)
le = LabelEncoder()
for i in categorical_features:
    train[i] = le.fit_transform(train[i])
data = train.select_dtypes(include=[np.number]).interpolate().fillna(train.select_dtypes(include=[np.number]).interpolate().mean(axis=0))
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(data)
X_train = scaler.transform(data)

from sklearn.cluster import KMeans
nclusters = 3
seed = 0
km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_train)
y_cluster = km.predict(X_train)

from sklearn import metrics
score = metrics.silhouette_score(X_train, y_cluster)
scores = metrics.silhouette_samples(X_train, y_cluster)
print("Silhoutte score",score)

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++', max_iter=300, n_init=10,random_state=0)
    kmeans.fit(data)
    cluster_an = kmeans.predict(data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

plt.scatter(y_cluster, scores, alpha=.75,
            color='b')
plt.xlabel('Cluster')
plt.ylabel('Scores')
plt.show()

plt.scatter(range(1,len(y_cluster)+1), y_cluster, alpha=.75,
            color='b')
plt.xlabel('Id')
plt.ylabel('Cluster')
plt.show()

plt.hist(y_cluster,color="blue")
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('K-Means Model')
plt.show()

data['category']=y_cluster;
sns.FacetGrid(data, hue="category", size=4).map(plt.scatter, "carat", "price").add_legend()
plt.show()

data['category']=y_cluster;
sns.FacetGrid(data, hue="category", size=4).map(plt.scatter, "cut", "price").add_legend()
plt.show()
