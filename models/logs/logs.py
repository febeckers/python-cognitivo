from datetime import datetime
import os, logging

class Logs:
  
	def __init__(self):
		log_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
		log_path = os.path.join(os.getcwd(), 'logs', str(log_name)) + ".log"
		logger = logging.getLogger()
		logger.setLevel(logging.INFO)
		handler = logging.FileHandler(log_path, 'w', 'utf-8')
		formater = logging.Formatter('%(asctime)s | %(message)s')
		handler.setFormatter(formater)
		logger.addHandler(handler)
		Logs.i(f'LOGS | file in {log_path}')
		pass

	def i(msg):
		msg if type(msg) is str else str(msg)
		logging.info(f'LOGS | INFO | {msg}')
		pass

	def w(msg):
		msg if type(msg) is str else str(msg)
		logging.warning(f'LOGS | WARNING | {msg}')
		pass

	def e(msg):
		msg if type(msg) is str else str(msg)
		logging.error(f'LOGS | ERRROR | {msg}')
		pass




