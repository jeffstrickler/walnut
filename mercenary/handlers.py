__author__ = 'jeffstrickler - jeff@mercenarytech.com'
__copyright__ = "Copyright (C) 2013 Mercenary Technologies LLC"


import logging
import json
import tornado.web

from mercenary.models import *


logger = logging.getLogger("walnut")



class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return None



class LoadHandler(BaseHandler):
    """ trivial example to show loading the trie from a database """
    def get(self):
        logger.info("LoadHandler:get()")
        users = self.application.persistence.query_all(User)
        if users:
            for user in users:
                self.application.trie[user.username] = 0
        self.set_status(200)
        self.write(json.dumps(len(self.application.trie)))
        self.finish()

    def post(self):
        logger.info("LoadHandler:post()")
        users = self.application.persistence.query_all(User)
        for user in users:
            self.application.trie[user.username] = 0
        self.set_status(200)
        self.write(json.dumps(len(self.application.trie)))
        self.finish()


class AddHandler(BaseHandler):
    """ Add an item to the trie """
    def get(self, key):
        logger.info("AddHandler:get()")
        self.application.trie[key] = 0
        self.set_status(200)
        self.finish()

    def post(self,key):
        logger.info("AddHandler:post()")
        self.application.trie[key] = 0
        self.set_status(200)
        self.finish()


class CountHandler(BaseHandler):
    """ Get the current number of items in the trie """
    def get(self):
        logger.info("CountHandler:get()")
        self.set_status(200)
        self.write(json.dumps(len(self.application.trie)))
        self.finish()

    def post(self,key):
        pass


class AllHandler(BaseHandler):
    """ get a list of all keys in the trie """
    def get(self):
        logger.info("AllHandler:get()")
        self.set_status(200)
        self.write(json.dumps(self.application.trie.keys()))
        self.finish()

    def post(self):
        pass



class ExistsHandler(BaseHandler):
    """ Does the received key exist in the trie? """
    def get(self, key):
        logger.info("ExistsHandler:get()")
        self.set_status(200)
        #self.set_header("Content-Type", "application/json")
        self.write({json.dumps(key in self.application.trie)})
        self.finish()

    def post(self,key):
        pass


class ContainsHandler(BaseHandler):
    """ Return a list of keys that match the received prefix """
    def get(self, key):
        logger.info("ContainsHandler:get()")
        self.set_header("Content-Type", "application/json")
        self.set_status(200)


        #self.write(json.dumps({'contains':self.application.trie.keys(key)}))
        self.write(json.dumps(self.application.trie.keys(key)))
        self.finish()

    def post(self,key):
        pass
