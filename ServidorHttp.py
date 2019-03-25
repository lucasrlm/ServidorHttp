#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
from ConversorInteiroParaExtenso import *
import json
 
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Status code da resposta
        self.send_response(200)
 
        # Header da resposta
        self.send_header('Content-type','application/json')
        self.end_headers()

        try:
            val = self.path.split('/',1)[1]
            valExtenso = converterInteiroParaExtenso(int(val))

            # Resposta em json
            resposta = {'extenso':valExtenso}
            self.wfile.write(bytes(json.dumps(resposta), "utf8"))
            return

        except ValueError as err:
            # Resposta em json
            resposta = {'erro':err.args[0]}
            self.wfile.write(bytes(json.dumps(resposta), "utf8"))
 
def run():
  print('Inicializando servidor...')
 
  server_address = ('0.0.0.0', 8181)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
  print('Servidor rodando...')
  httpd.serve_forever()
 
 
run()