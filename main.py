from models.manipulation.files import Files
from models.logs.logs import Logs
from models.database.aplications import Aplications

if __name__ == '__main__':

	try:

		Logs()
		Aplications()
		files = Files()
		
		file_name = '2022-10-11-06-00.csv'

		if files.exists( file_name ):
			file = files.read( file_name )
			print(file)
	
	except  Exception as e:
		Logs.e(e)
	finally:
		print("F I N I S H E D")