from models import Samples

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import json

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "tp2"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()

    def get_last(self):
        ultima=0
        #session = self.get_session()
        #ultima = session.query(Samples).order_by(Samples.id.desc()).first()
        #session.close()
        return ultima
    ################################

    def get_last_ten(self):
        promedio=0
        #promedio = Samples()
        #promedio.temperature = 0
        #promedio.humidity = 0
        #promedio.pressure = 0
        #promedio.windspeed = 0
        #session = self.get_session()
        #diez = session.query(Samples).order_by(Samples.id.desc()).limit(10)
        #session.close()
        #for d in diez:
        #    promedio.temperature = (promedio.temperature + d.temperature)
        #    promedio.humidity = (promedio.humidity + d.humidity)
        #    promedio.pressure = (promedio.pressure + d.pressure)
         #   promedio.windspeed = (promedio.windspeed + d.windspeed)
        #promedio.temperature = (promedio.temperature/10)
        #promedio.humidity = (promedio.humidity/10)
        #promedio.pressure = (promedio.pressure/10)
        #promedio.windspeed = (promedio.windspeed/10)
        return promedio
    ################################

    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    