from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Gaya@123@localhost/students'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
import psycopg2

def get_connection():
	try:
		return psycopg2.connect(
			database="postgres",
			user="postgres",
			password="Gaya@123",
			host="127.0.0.1",
			port=5432,
		)
	except:
		return False

conn = get_connection()

if conn:
	print("Connection to the PostgreSQL established successfully.")
else:
	print("Connection to the PostgreSQL encountered and error.")

from app import routes