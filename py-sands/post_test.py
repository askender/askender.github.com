#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")

    def post(self):
        obj = json.loads(self.request.body)
        args = json.dumps(obj)
        print('%s\nI got it' % args)

handlers = [
    (r"/", MainHandler),
]
web_server = {
    'debug': True,
}

application = tornado.web.Application(handlers, **web_server)

if __name__ == "__main__":
    application.listen(8004)
    tornado.ioloop.IOLoop.instance().start()
