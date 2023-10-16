from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://admin:9BjfPJJVkU3qa74h@cluster0.yonaobp.mongodb.net/?retryWrites=true&w=majority"

client =MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
	print(db_name)