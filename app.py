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

class CalculatorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", result=None, num1=None, num2=None, operation=None)
    def post(self):
        operation = self.get_argument("operation")
        num1 = float(self.get_argument("num1"))
        num2 = float(self.get_argument("num2"))

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        elif operation == "subtract":
            result = num1 - num2
        else:
            self.set_status(400)  
            self.write({"error": "Invalid operation."})
            return 
        print("Result :", result)
        self.render("index.html", result=result, num1=num1, num2=num2, operation=operation)
        


def make_app():
    return tornado.web.Application([
        (r"/", HelloWorldHandler),
        (r"/sum", SumHandler),
        (r"/calculator", CalculatorHandler)
    ], template_path="./templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
