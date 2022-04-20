# Using the sqlalchemy core features to
from sqlalchemy import Column, Integer, String, create_engine,text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True, echo_pool='debug', logging_name='myengine')

with engine.connect() as conn:
    print(conn.scalar(text("select 'hi'")))

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))


Base.metadata.create_all(engine)

with engine.connect() as connection:
    result = connection.execute(text("select username from users"))
    for row in result:
        print("username:", row['username'])
# END OF EXAMPLES
