import tornado.ioloop
import tornado.web

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

def make_app():
    return tornado.web.Application([
        (r"/", HelloWorldHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
