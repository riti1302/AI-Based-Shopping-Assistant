import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift # as ms
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from collections import Counter


centers = [[1,1],[5,5],[8,4]]

dataset = pd.read_csv('person.csv')

X = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,[0]].values
name = dataset['Item_names'].tolist()

plt.scatter(X[:,0], X[:,1])
plt.show()

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

#print(cluster_centers)

gg = Counter(labels)
#print(gg)

def find_max():
	max = gg[0]
	v = 0
	for i in range(len(gg)):
		if gg[i] > max:
			max = gg[i]
			v = i
	return v

#print(type(labels))
Y = y.tolist()
L = labels.tolist()

max_label = find_max()
#print("max_label",max_label)

suggest = []
for i in range(len(labels)):
	if max_label == L[i]:
		suggest.append(Y[i])

new = []

def stripp(rr):
	for i in range(len(suggest)):
		p=str(rr[i]).replace('[','').replace(']','')
		new.append(int(p))
	return new

new_Y = stripp(Y)
new_name = []
for i in range(len(suggest)):
		p=str(name[i]).replace('[','').replace(']','')
		new_name.append(p)


#print("new_y", new_Y[4])
#print("Y" ,p[0])
#print(Y, L)
#print(len(suggest))
#print("suggest array::",suggest)

n_clusters_ = len(np.unique(labels))

#print("Number of estimated clusters: ", n_clusters_)

colors = 10*['r.','g.','b.','c.','k.','y.','m.']

#print(colors)
#print(labels)

for i in range(len(X)):
	plt.plot(X[i][0], X[i][1], colors[labels[i]],markersize = 10)

plt.scatter(cluster_centers[:,0],cluster_centers[:,1], marker = "x", s=150, linewidths = 5, zorder=10)


item_name = dict(zip(new_Y, new_name))
#print("item_name   ", item_name)

plt.show()
