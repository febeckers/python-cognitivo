from models.logs.logs import Logs
from models.database.database import Database

from sqlalchemy import Column, Integer, String, Float, MetaData, Table

class Aplications(Database, Logs):

	def __init__(self) -> None:
		
		database = Database()
		engine = database.conection()
		
		meta_data = MetaData()

		Table('aplications', 
					meta_data,
					Column('id', Integer, primary_key=True, autoincrement=True),
					Column('tack_name', String(100)),
					Column('size_byte', Integer),
					Column('currency', String(100)) )
		meta_data.create_all(engine)
		pass