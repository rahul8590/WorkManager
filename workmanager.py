#The workmanager is reposible for spawning various worker process 
# which could either run in localhost itself , or in other hosts 
#


import simplejson , sys , os

#wid =  worker id 
#host = List of host
#pool = total no_of_workers to be spawned 
#wphost = worker per host to be spawned 
#nhost = total no of host



class workmanager:


	def __init__ ( self , wid ,host,pool,wphost,nhost ):
		self._wid = wid
		self._pool = pool
		self._wphost = wphost
		self._nhost = 0
		self._host = []


	def allocate():
		json_data = open("work_config.json").read(()
		data = simplejson.loads(json_data)
		self._pool = data['pool']
		for i in data['no_of_worker'].split(','): 
			self._nhost += 1
			self._host.append(i)
		self._wphost = self._pool/self._nhost
	

	def runworker():
		
			
		
		
  
