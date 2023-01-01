from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)   
database = "postgres"
username = "postgres"
password = "Gaya"
host = "127.0.0.1"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}:5432/{database}"
# app.config["SQLALCHEMY_DATABASE_URI"] = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="Gaya@123",
#     host="127.0.0.1",
#     port=5432,
# )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
db=SQLAlchemy(app)
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

from app import routes