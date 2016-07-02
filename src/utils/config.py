import json

class Config(object):

	def __init__(self, config_file):
		config = self._from_file(config_file)

		self.plotly_username = config["plotly"]["username"]
		self.plotly_api_key = config["plotly"]["api_key"]

		self.data_filename = config["data_filename"]

	def _from_file(self, config_file):
		config_file = open(config_file)
		config = json.load(config_file)['config']
		return config