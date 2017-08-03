# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:21:53 2017

@author: M1033778
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name':['Tim','Jim','Pam','Sam'],
		'age':[29,31,27,35],
		'ZIP':['02115','02130','67700','001100']}

y = pd.Series([6,4,8,6], index=["q","w","e","r"])
y.reindex(sorted(y.index))

z = pd.Series([6,4,8,6], index=["e","q","r","t"])

whisky = pd.read_csv("D:/Anaconda2/whiskies.txt")
whisky["Region"] = pd.read_csv("D:/Anaconda2/regions.txt")
#firsr argument correspond to rows
whisky.iloc[5:10, 0:5]
#second arguments correspond to columns
whisky.iloc[5:10, 0:5]

flavors = whisky.iloc[:,2:14]

corr_flavors = pd.DataFrame.corr(flavors)
print (corr_flavors)

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)

np.sum(model.rows_,axis=1)

model.row_labels_

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)

whisky = whisky.ix[np.argsort(model.row_labels_)]

whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())

correlations = np.array(correlations)


















