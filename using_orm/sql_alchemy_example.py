# Practive sqlAchemy functionality.
# Using the ORM - Object Relational Mapping feature to access the database using sqlAlchemy
from typing import Union, Any

from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import Session, DeclarativeMeta
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

# Create an engine, which is a driving component that uses mapper and pooling to
# communicate to the underlying respective DBAPI which inturn queries/communicates the database
# Flow:
#           Engine -> Pooling,Mapper -> DBAPI -> Database
engine: Union[MockConnection, Any] = create_engine('sqlite:///workspace.db', echo=True, echo_pool='debug', logging_name='myengine')

# The session is responsible for maintaining transactions and
# each execution is a transaction inside a session
session: Session = Session(bind=engine)

# Base holds all the metadata, schema and column information for
# the tables that we intend to create
Base: Union[DeclarativeMeta, Any] = declarative_base()

# cookie = Base.classes.Cookie
# print(session.query(cookie).all())


# The class that inherited from Base class can be used/equivalent to the table DDL
# These classes will be directly converted to DDL statement in the backend when
# Base.metadata.create_all(engine) is called (as below)
class Cookie(Base):
    __tablename__ = "cookies"

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50))
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Integer())


# Base stores all the metadata from the class that extends Base class.
# Below command create the table with all the classes as the DDL and
# the columns inside the classes as actual columns
Base.metadata.create_all(engine)

# Creating the instance of the class `Cookie` which
# is mapped to row in the database context
add_new_data = True
if add_new_data:
    aCookie1: Cookie = Cookie(
        cookie_name="aCookie1",
        cookie_recipe_url="aCookieURL",
        cookie_sku="01SKU",
        quantity=10,
        unit_cost=100
    )

    # Adding the row to the session.
    session.add(aCookie1)

# Querying the added row and printing the data retrieved.
result: object = session.query(Cookie).all()
for records in result:
    print(records.cookie_id, records.cookie_name, records.cookie_recipe_url, records.cookie_sku, records.quantity,
          records.unit_cost)

# Accessing specific columns.
specific_columns: object = session.query(Cookie.cookie_name, Cookie.quantity).all()
print(specific_columns)

# Deleting the contents of the table.
delete: bool = False
if delete:
    session.query(Cookie).delete()

# Commit triggers all the execution starting from the actual data insertion.
# It begins the transaction and executes the above insert, select and delete statements.
# Commit - commits the transaction if successful, rollback in case of any failures
session.commit()
