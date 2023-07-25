import json
import tornado.ioloop
import tornado.web

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

class SumHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            numbers = data.get("numbers", [])
            if isinstance(numbers, list):
                numbers_sum = sum(numbers)
                self.write({"sum": numbers_sum})
            else:
                self.set_status(400)  # Bad Request
                self.write({"error": "Data must contain a list of numbers."})
        except json.JSONDecodeError:
            self.set_status(400)  # Bad Request
            self.write({"error": "Invalid JSON format."})
        

def make_app():
    return tornado.web.Application([
        (r"/", HelloWorldHandler),
        (r"/sum", SumHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
