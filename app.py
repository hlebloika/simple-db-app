import os

from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(os.getenv('DATABASE_URL'))

@app.route("/")
def hello_world():
    return f"DB string - {os.getenv('DATABASE_URL')}"