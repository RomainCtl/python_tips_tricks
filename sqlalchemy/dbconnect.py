from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from functools import wraps
# from config import Config
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@host:port/schema'
    MYSQL_DATABASE_CHARSET = 'utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_TIMEOUT = 20

Session = scoped_session(sessionmaker(bind=create_engine(Config.SQLALCHEMY_DATABASE_URI), autoflush=True))

def dbconnect(func):
    @wraps(func)
    def inner(*args, **kwargs):
        current_session = Session()
        try:
            res = func(*args, session=current_session, **kwargs)
            current_session.commit()
        except Exception as e:
            current_session.rollback()
            if len(e.args) > 0: res = dict(message=type(e).__name__ +": "+e.args[0]), e.args[1] if len(e.args) > 2 else 500
            else: res = dict(message=type(e).__name__ +": "+str(e)), 500
                
            # print traceback (may use a logger)
            traceback.print_tb(e.__traceback__)
            print(res['message'])
        finally:
            current_session.close()
            Session.remove()
            return res
    return inner
