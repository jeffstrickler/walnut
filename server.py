__author__ = 'jeffstrickler - jeff@mercenarytech.com'
__copyright__ = "Copyright (C) 2013 Mercenary Technologies LLC"


import logging
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import os

import string
import datrie

import mercenary.persistence

from mercenary.handlers import *




define("port", default=8888, help="run on the given port", type=int)
define ("log_path", default="./walnut.log", help="path to logfile")
define("database_name", default="my_database_name")
define("database_host", default="127.0.0.1")
define("database_user", default="jeffstrickler")
define("database_password", default="password")



class Application(tornado.web.Application):

   
    def __init__(self):

        settings = {
            "debug":"Yes",
        }

        handlers = [
            (r"/load", LoadHandler),
            (r"/add/(.*)", AddHandler),
            (r"/exists/(.*)", ExistsHandler),
            (r"/contains/(.*)", ContainsHandler),
            (r"/all", AllHandler),
            (r"/count", CountHandler),

        ]

        self.persistence = mercenary.persistence.Persistence(options.database_name, options.database_host, options.database_user, options.database_password)
        """ if you want to put something into this trie other than integers, make this into a Trie instead of a BaseTrie """
        self.trie = datrie.BaseTrie(string.ascii_lowercase)

        #create logger
        logger = logging.getLogger("walnut")
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(options.log_path)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("{'timestamp': %(asctime)s, 'loglevel' : %(levelname)s %(message)s }")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        tornado.web.Application.__init__(self, handlers, **settings)

        logger.info("Application started")


def main():

    config = tornado.options.parse_command_line()

    io_loop = tornado.ioloop.IOLoop.instance()

    tornado.options.parse_config_file("etc/"+config[0]+".conf")
    application = Application()

    application.listen(options.port)
    io_loop.start()


if __name__ == "__main__":
    main()
