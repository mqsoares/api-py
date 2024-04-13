from pymongo import MongoClient

# MySQL
SQLALCHEMY_DATABASE_URI = 'mysql://root:1234qwer@localhost:3306/db_posweb'

# Mongo
cliente = MongoClient('mongodb://localhost:27017')
mongodb = cliente['posweb']
pedidos_collection = mongodb['pedidos']