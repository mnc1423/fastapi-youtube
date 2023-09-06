import os

from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from dotenv import load_dotenv
from databases import Database
from datetime import datetime as dt
from pytz import timezone as tz

load_dotenv()
# Database url if none is passed the default one is used
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hello_fastapi:hello_fastapi@localhost/hello_fastapi_dev")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url_list", String(50)),
    Column("vid_title", String(50)),
    Column("videoID",String(16), default="False"),
    Column("timestamp", String(50))
)
# Databases query builder
database = Database(DATABASE_URL)
