from models.logs.logs import Logs

import pandas as pd
import os

class Files(Logs):

	def __init__(self):
		pass

	def exists(self, file_name):
		file_path_full = os.path.join(os.getcwd(), 'files', file_name )
		if os.path.exists(file_path_full):
			Logs.i(f'FILES | file exits {file_path_full}')
			return True
		else:
			Logs.i(f'FILES | file not exits {file_path_full}')
			return False
	
	def read(self, file_name):
		file_path_full = os.path.join(os.getcwd(), 'files', file_name )
		return pd.read_csv(file_path_full)