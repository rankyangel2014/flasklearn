from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app
from tornado.options import define, options
import tornado.options

define("port", default=8080, help="port to listen on")

tornado.options.parse_command_line()
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(options.port)
IOLoop.instance().start()
