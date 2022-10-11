from models.logs.logs import Logs

from dotenv import load_dotenv, dotenv_values, find_dotenv

import sqlalchemy as sql
import os

class Database(Logs):

	engine  = None
	
	mysql_host = None
	mysql_port = None
	mysql_user = None
	mysql_password = None
	mysql_database = None

	def __init__(self) -> None:

		dotenv_path = os.path.join(os.getcwd(), ".env")
		load_dotenv(dotenv_path)
		Logs.i('DATABASE | SQLA version ' + sql.__version__)
		pass
		
	def conection(self):

		mysql_host = os.getenv("MYSQL_HOST")
		mysql_port = os.getenv("MYSQL_PORT")
		mysql_user = os.getenv("MYSQL_USER")
		mysql_password = os.getenv("MYSQL_PASSWORD")
		mysql_database = os.getenv("MYSQL_DATABASE")

		engine = sql.create_engine(f'mysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}', echo=True)
		return engine