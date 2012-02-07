#The workmanager is reposible for spawning various worker process 
# which could either run in localhost itself , or in other hosts 
#the worker.py module is been imported and will be executed in the slave.


import simplejson , sys , os
import worker
from fabric  import * 
from fabric.api import *
import gevent

#wid =  worker id 
#host = List of host
#pool = total no_of_workers to be spawned 
#wphost = worker per host to be spawned 
#nhost = total no of host



path_file = '/home/y/workmanager/worker.py'

class workmanager:


	def __init__ ( self , wid ,host,pool,wphost,nhost,cmd):
		self._wid = wid
		self._pool = pool
		self._wphost = wphost
		self._nhost = 0
		self._host = host
		self._cmd = 'python '+path_file

	#calibrates the meterics afore mentioned. 
	def allocate():
		json_data = open("work_config.json").read(()
		data = simplejson.loads(json_data)
		self._pool = data['pool']
		for i in data['no_of_worker'].split(','): 
			self._nhost += 1
			self._host.append(i)
		self._wphost = self._pool/self._nhost




		
#instantiate  worker instances. 
def runworker(host):
	env.host_string = host
	j = 0
	while j < self._wphost:
		run (self._cmd)
		j += 1 


#Program to check the status of the status workers
def check_status():
	




def main():
	work = workmanager()
	work.allocate()
	jobs = [gevent.spawn( work.runworker , h) for h in work.host ] 
	gevent.joinall()
	


if __name__ == '__main__':
    main()






		

	
		



		
			
	
		
		
			
		
		
  
