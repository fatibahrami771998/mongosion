#-*- coding: UTF-8 -*-

import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import os.path
import json
import time
import random
import os

# cookie_secret
import base64 
import uuid 
import hashlib 

import mongosion

define("port", default=8880, help="run on the given port", type=int)
define("db", default='mongosion', help="database name", type=str)

class Application(tornado.web.Application):
    '''setting || main || router'''
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        
        settings = dict(
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            base_path=os.path.join(os.path.dirname(__file__), ""),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    ''' init for handlers '''
    def initialize(self):
    	# get session id from cookie
        self.session_id = self.get_secure_cookie("sid")
       	
        # get sesson from mongosion 
        self.data = mongosion.get(self.session_id)

        # update session id in cooike
        self.session_id = self.data['_id']
        self.set_secure_cookie("sid",self.data['_id'])

    def get(self):

    	#self.write(mongosion.get(self.session_id))
		self.write('<html><body><h4>save a session </h4>')
		data = mongosion.save( self.data['_id'], {'uid':'123', 'name':'YaoHomeway', 'status':'forbidden'})

		self.write('<h4>result :</h4>')
		self.write(data)
		self.write('<h4>delete a session </h4>')

		flag = mongosion.delete(data['_id'])

		self.write('<h4>delete successfully</h4><body></html>')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main() 















