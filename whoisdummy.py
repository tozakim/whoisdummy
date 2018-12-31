#!/usr/bin/env python
import sys
import SocketServer 

class WhoisDummyHandler(SocketServer.StreamRequestHandler):
	def write(self, stream_data):
		self.request.sendall(bytes(stream_data))

	def handle(self):
		self.data = self.rfile.readline().strip()
		print self.data
		self.wfile.write("hello")

if __name__ == "__main__":
	HOST, PORT = "0.0.0.0", 43
	
	server = SocketServer.TCPServer((HOST, PORT), WhoisDummyHandler)
	server.serve_forever()
