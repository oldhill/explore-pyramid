from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
  """ yeeep
  """
  print ('Incoming request')
  return Response('<body><h1>Hello World!</h1></body>')


if __name__ == '__main__':
  # set up server etc

  config = Configurator()

  # route
  my_route_name = 'hello'
  config.add_route(my_route_name, '/')
  config.add_view(hello_world, route_name=my_route_name)

  app = config.make_wsgi_app()
  server = make_server('127.0.0.1', 6543, app)  # localhost only
  server.serve_forever()
