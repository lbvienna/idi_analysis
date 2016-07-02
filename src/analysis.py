from utilities import *

from sklearn import decomposition
import matplotlib.pyplot as plt


def main(filename):
	data = read_csv(filename)
	data = convert_numeric(data)
	numerics = np.asarray(data[:,4:], dtype=np.float32)
	svd(numerics)
	pca(numerics, n_components=3)

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
		from mpl_toolkits.mplot3d import Axes3D
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		plt.scatter(X[:, 0], X[:, 1], X[:, 2])
		plt.show()

if __name__ == '__main__':
	filename = "data/idi_data.csv"
	main(filename)