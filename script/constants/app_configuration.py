import configparser
parser = configparser.RawConfigParser()
parser.read(r"C:\Users\varsha.ks\PycharmProjects\pythonProject15\configuration\database.conf")

mongo_uri = parser.get('MONGODB', 'mongo_uri')
db = parser.get('MONGODB', 'db_name')
