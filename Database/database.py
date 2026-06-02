import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os
conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password=os.getenv("password"),
    database=os.getenv("database")
)

cursor = conn.cursor()

print("Connected successfully")