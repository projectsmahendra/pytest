import  os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    DB_USER = os.getenv('DB_USER','pytest')
    DB_NAME = os.getenv('DB_NAME','pytestdb')
    DB_PASS = os.getenv('DB_PASS','123abc')
    SQLALCHEMY_DATABASE_URI = conn_str = 'postgresql://{username}:{password}@localhost:5432/{database}'.format(
            username=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )

