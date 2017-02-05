"""
Description:  The program receives a csv file

              Computes clustering of jet contituents with K-Means

              Returns a plot with syntax name run_lumi_event.png


Requirements: Pandas Data Analysis Library (http://pandas.pydata.org)

              scikit-learn: Machine Learning in Python (http://scikit-learn.org)

              Python 3.X 


Usage:        python3 analyze_csvFiles.py run_lumi_event

"""

import sys
import math
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Pick data
data = pd.read_csv('csvFiles/'+sys.argv[1]+'.csv')

# Get cartesian coordinates
X = data[['Px','Py','Pz']].as_matrix()

# Cosmetics
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(16,4), sharey=True)
axes[0].set_title('Real classification')

# Plot real classification
for i in data.Jet.unique():
    jet = data[data.Jet == i] 
    jet.plot.scatter(x='Eta', y='Phi', color=colors[i], label='Jet %d'%(i), ax=axes[0])

# Compute clustering with K-Means
for k in range(1,5):
    model = KMeans(init='k-means++', n_clusters=k)
    model.fit_predict(X)
    data['Prediction'] = model.labels_
    axes[k].set_title('%d cluster classification'%(k))
    # Plot K-Means prediction
    for i in data.Prediction.unique():
        jet = data[data.Prediction == i] 
        jet.plot.scatter(x='Eta', y='Phi', color=colors[i], label='Jet %d'%(i), ax=axes[k])

plt.tight_layout()
plt.savefig('outPlots/'+sys.argv[1]+'.png')
plt.close()
