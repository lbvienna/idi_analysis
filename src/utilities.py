import csv
import numpy as np

def read_csv(file_, sep=','):
	data = []
	with open(file_, 'rb') as csv_file:
		reader = csv.reader(csv_file, delimiter=sep)
		for i, row in enumerate(reader):
			if i == 0:
				continue
			data.append(row)
	return np.asarray(data)

def convert_numeric(data):
	new_data = []
	for row in data:
		new_row = []
		for x_ij in row:
			try:
				new_x_ij = int(x_ij)
			except ValueError:
				if x_ij == "NA": # decide what to do with NA data
					new_x_ij = 0
				else:
					new_x_ij = x_ij
			new_row.append(new_x_ij)
		new_data.append(new_row)
	return np.asarray(new_data)
