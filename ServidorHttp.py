#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
from ConversorInteiroParaExtenso import *
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        try:

            val = self.path.split('/',1)[1]
            valExtenso = converterInteiroParaExtenso(int(val))

            # Write content as utf-8 data
            self.wfile.write(bytes(valExtenso, "utf8"))
            return

        except ValueError as err:
            self.wfile.write(bytes(err.args[0], "utf8"))
 
def run():
  print('Inicializando servidor...')
 
  server_address = ('127.0.0.1', 3000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('Servidor rodando...')
  httpd.serve_forever()
 
 
run()