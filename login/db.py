from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, String, Integer

metadata = MetaData()
engine = create_engine('sqlite:///mydb.db', echo=True, future=True)

user_table = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(30), nullable=False, unique=True),
    Column('password', String(30), nullable=False)
)


def init_db():
    metadata.create_all(engine)