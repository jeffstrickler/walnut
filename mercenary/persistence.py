__author__ = 'jeffstrickler - jeff@mercenarytech.com'
__copyright__ = "Copyright (C) 2013 Mercenary Technologies LLC"

import sqlalchemy
from sqlalchemy.orm import sessionmaker
import logging


logger = logging.getLogger("walnut")

class Persistence:
    engine = None
    session = None

    def __init__(self, database, hostname, username, password, pool_size=20):
        self.engine = sqlalchemy.create_engine('postgresql+psycopg2://'+username+':'+password+'@'+hostname+'/'+database, pool_size=pool_size, max_overflow=0)

    def __session(self):
        if (self.session == None):
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        return self.session

    def get_session(self):
        return self.__session()


    def query_all(self, model):
        thing = None
        try:
            thing = self.__session().query(model).all()

        except Exception as e:
            logger.info(e)
        return thing


