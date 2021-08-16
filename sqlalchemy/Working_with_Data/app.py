from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey

metadata = MetaData()

user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)


address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
metadata.create_all(engine)

from sqlalchemy import insert, select

stmt = insert(user_table).values(name='spongebob', fullname='Spongbob Squarepants')

print(stmt)

compiled = stmt.compile()
print(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()


with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ]
    )
    conn.commit()

select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)