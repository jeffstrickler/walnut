__author__ = 'jeffstrickler - jeff@mercenarytech.com'
__copyright__ = "Copyright (C) 2013 Mercenary Technologies LLC"

import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.interfaces import MapperExtension

Base = declarative_base()


class BaseExtension(MapperExtension):

    def before_insert(self, mapper, connection, instance):
        instance.created = datetime.datetime.now()

    def before_update(self, mapper, connection, instance):
        instance.last_modified = datetime.datetime.now()


class User(Base):
    __tablename__ = 'users'
    __mapper_args__ = { 'extension': BaseExtension() }
    id = Column(Integer,  Sequence('users_id_seq'), primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    last_modified = Column(DateTime)
    created = Column(DateTime)

    def __init__(self, firstName, lastName, email, username,password):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return self.first_name + " " + self.last_name + " " + self.email

    def __unicode__(self):
        return self.first_name + " " + self.last_name + " " + self.email

