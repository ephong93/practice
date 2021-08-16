from sqlalchemy import create_engine

# 모든 sqlalchemy application은 Engine으로 시작한다.
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
# memory: 메모리 위에서 동작
# echo: log 출력
# future: 2.0 기능 사용

# sqlite database 사용.
# pysqlite DBAPI 사용.


# Connection, Result, Session
# SQLAlchemy Expression Language를 사용하기 전에 일단 textual SQL로 설명


# Getting a Connection
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

# transaction은 자동으로 commit되지 않는다.

# Commiting Changes

# commit as you go
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()

# begin once
# sopce가 끝나면 자동으로 commit
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )


with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")

    for dict_row in result.mappings():
        x = dict_row['x']
        y = dict_row['y']

# Sending Parameters
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT x, y FROM some_table WHERE y > :y"),
        {"y": 2}
    )
    for row in result:
        print(f"x: {row.x} y: {row.y}")

# SQL injection을 예방하기 위해 항상 bound parameter를 사용해야 한다.


#Bundling Parameters with a Statement
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x} y: {row.y}")

# Executing with an ORM Session
from sqlalchemy.orm import Session

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER by x, y").bindparams(y=6)
with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x: {row.x} y: {row.y}")


# Session은 commit as you go임
with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
    )
    session.commit()