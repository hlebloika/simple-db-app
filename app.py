import os

from flask import Flask
from sqlalchemy import create_engine, MetaData, Table, Integer, String

app = Flask(__name__)

engine = create_engine(os.getenv('DATABASE_URL'))
metadata_obj = MetaData()

message_table = Table(
    "test",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("message", String)
)

metadata_obj.create_all(engine)

@app.route("/")
def hello_world():
    return f"DB string - {os.getenv('DATABASE_URL')}"