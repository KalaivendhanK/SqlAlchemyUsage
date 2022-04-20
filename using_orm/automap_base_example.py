from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:///workspace.db', echo=True, echo_pool='debug', logging_name='myengine')

Base = automap_base()
Base.prepare(engine)

session = Session(bind=engine)

base_cookie = Base.classes.cookies

cookies = session.query(base_cookie.cookie_id, base_cookie.cookie_name, base_cookie.quantity).all()

for cookie in cookies:
    print(cookie)


session.commit()
