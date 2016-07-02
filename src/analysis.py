from utils import utilities, config

import argparse

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import decomposition

from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist

import plotly.plotly as py
import plotly.graph_objs as go



def main(filename):
	data = utilities.read_csv(filename)
	data = utilities.convert_numeric(data)
	numeric_start = 4
	basic_questions_end = 13
	numerics = np.asarray(data[:,numeric_start:basic_questions_end], dtype=np.float32)
	#svd(numerics)
	pca(numerics, n_components=3)
	#k_means(numerics)

def svd(data):
	U, s, V = np.linalg.svd(data, full_matrices=True)
	print s

def pca(data, n_components=2):
	pca = decomposition.PCA(n_components=n_components)
	pca.fit(data)
	X = pca.transform(data)
	if n_components == 2:
		plt.scatter(X[:, 0], X[:, 1])
		plt.show()
	else:
		# doesn't work. some really strange bug

		trace1 = go.Scatter3d(
		    x=X[:, 0],
		    y=X[:, 1],
		    z=X[:, 2],
		    mode='markers',
		    marker=dict(
		        size=12,
		        line=dict(
		            color='rgba(217, 217, 217, 0.14)',
		            width=0.5
		        ),
		        opacity=0.8
		    )
		)
		data = [trace1]
		layout = go.Layout(
    		margin=dict(
        	l=0,
        	r=0,
        	b=0,
        	t=0
    		)
		)
		fig = go.Figure(data=data, layout=layout)
		py.iplot(fig, filename='simple-3d-scatter')

def k_means(data, K=range(1,10)):
	if type(K) is list:
		KM = [kmeans(data,k) for k in K]
		centroids = [cent for (cent,var) in KM]

		D_k = [cdist(data, cent, 'euclidean') for cent in centroids]
		cIdx = [np.argmin(D,axis=1) for D in D_k]
		dist = [np.min(D,axis=1) for D in D_k]
		avgWithinSS = [sum(d)/data.shape[0] for d in dist]
		
		kIdx = 2

		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(K, avgWithinSS, 'b*-')
		ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, 
    		markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
		plt.grid(True)
		plt.xlabel('Number of clusters')
		plt.ylabel('Average within-cluster sum of squares')
		plt.title('Elbow for KMeans clustering')

		plt.show()
	elif type(K) is int:
		KM = kmeans(data,K)
		centroids, var = KM

		D_k = cdist(data, centroids, 'euclidean')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', dest='config_file', default='conf/index.json', help='use specified config file')
	args = parser.parse_args()
	config = config.Config(args.config_file)

	utilities.plotly_login(config.plotly_username, config.plotly_api_key)

	main(config.data_filename)







