import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/updateprofile/alice">Alice</a><br>')
        self.write('<a href="/updateprofile/bob">Bob</a><br>')
        self.write('<a href="/updateprofile/carol">Carol</a><br>')
        self.write('<a href="/updateprofile/dave">Dave</a>')