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


""" trivial example to show loading the trie from a database """
class LoadHandler(BaseHandler):
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

""" Add an item to the trie """
class AddHandler(BaseHandler):
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

""" Get the current number of items in the trie """
class CountHandler(BaseHandler):
    def get(self):
        logger.info("CountHandler:get()")
        self.set_status(200)
        self.write(json.dumps(len(self.application.trie)))
        self.finish()

    def post(self,key):
        pass

""" get a list of all keys in the trie """
class AllHandler(BaseHandler):
    def get(self):
        logger.info("AllHandler:get()")
        self.set_status(200)
        self.write(json.dumps(self.application.trie.keys()))
        self.finish()

    def post(self):
        pass


""" Does the received key exist in the trie? """
class ExistsHandler(BaseHandler):
    def get(self, key):
        logger.info("ExistsHandler:get()")
        self.set_status(200)
        #self.set_header("Content-Type", "application/json")
        self.write({json.dumps(key in self.application.trie)})
        self.finish()

    def post(self,key):
        pass


""" Return a list of keys that match the received prefix """
class ContainsHandler(BaseHandler):
    def get(self, key):
        logger.info("ContainsHandler:get()")
        self.set_header("Content-Type", "application/json")
        self.set_status(200)


        #self.write(json.dumps({'contains':self.application.trie.keys(key)}))
        self.write(json.dumps(self.application.trie.keys(key)))
        self.finish()

    def post(self,key):
        pass
