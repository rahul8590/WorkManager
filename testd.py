#!/usr/bin/python

import sys , time 
from daemon import Daemon

class Mydeamon (Daemon):
	def run(self):
		while True:
			time.sleep(100)

if __name__ == "__main__":
	daemon = Mydeamon( '/tmp/daemon-example.pid')
	if 'start' == sys.argv[1]:
		daemon.start()
	if 'stop' == sys.argv[1]:
		daemon.stop()
	if 'restart' == sys.argv[1]:
		daemon.restart()
	else:
		print " unknow"

