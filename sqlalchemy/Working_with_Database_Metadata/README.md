- SQLAlchemy Core과 ORM의 중심 요소는 SQL Expression Language이다.
- SQL Expression Language query의 기초는 데이터베이스를 표현하는 python object이다. 이 object는 database metadata라고 불린다.
- 가장 많이 사용되는 object는 MetaData, Table, Column이다
- Core-oriented style, ORM-oriented style 에서 어떻게 사용되는지 알아본다.


# Setting up MetaData with Table objects
- Table is declared (코드에서 명시적으로 선언됨) or reflected

```python
from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, String

user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

print(user_table.c.name)
print(user_table.c.keys())
print(user_table.primary_key)

from sqlalchemy import ForeignKey

address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)
```


## Emitting DDL to the Database
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)

metadata.create_all(engine)
```

# Defining Table Metadata with the ORM

## Setting up the Registry
```python
from sqlalchemy.orm import registry
mapper_registry = registry()
print(mapper_registry.metadata)
```

### declarative base
```python
Base = mapper_registry.generate_base()
```

## Declaring Mapped Classes

```python
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

```
## Emitting DDL to the database
```python
mapper_registry.metadata.create_all(engine)
```
```python
Base.metadata.create_all(engine)
```

# Table Reflection
```python
some_table = Table("user_account", metadata, autoload_with=engine)
print(some_table)
```