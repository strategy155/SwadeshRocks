from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os.path import dirname, join, normpath


current_dir = join(dirname(dirname(normpath(__file__))), 'static')
engine_path = 'sqlite:///'+ current_dir
engine = create_engine(engine_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)