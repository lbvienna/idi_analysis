from utilities import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import decomposition

from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist



def main(filename):
	data = read_csv(filename)
	data = convert_numeric(data)
	numerics = np.asarray(data[:,4:], dtype=np.float32)
	#svd(numerics)
	#pca(numerics, n_components=2)
	k_means(numerics)

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
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(X[:, 0], X[:, 1], X[:, 2])
		ax.show()

def k_means(data, K=range(1,100)):
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
	filename = "data/idi_data.csv"
	main(filename)