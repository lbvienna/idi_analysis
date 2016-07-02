import csv
import numpy as np
import plotly

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

def plotly_login(username, api_key):
	plotly.tools.set_credentials_file(username=username, api_key=api_key)

def get_color(i, meta_data_type, meta_data):
	if meta_data_type == "location":
		return get_color_place(i, meta_data[:,1])
	if meta_data_type == "sex":
		return get_color_gender(i, meta_data[:,2])
	if meta_data_type == "age":
		return get_color_age(i, meta_data[:,3])

def get_color_place(i, places):
	place = places[i]
	if place == "Jerusalem":
		return "blue"
	if place == "Tel Aviv":
		return "red"
	if place == "North":
		return "green"
	if place == "South":
		return "cyan"
	if place == "Haifa":
		return "magenta"
	if place == "Judea and Samaria":
		return "yellow"
	if place == "Center":
		return "black"

def get_color_gender(i, genders):
	gender = genders[i]
	if gender == "male":
		return "blue"
	return "red"

def get_color_age(i, ages):
	age = ages[i]
	if age == "18-24":
		return "blue"
	if age == "25-34":
		return "red"
	if age == "35-44":
		return "green"
	if age == "45-54":
		return "cyan"
	if age == "55-64":
		return "magenta"
	if age == "65+":
		return "yellow"