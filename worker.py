#!/usr/bin/env python
import sys
import json
import gearman
from fabric import *
from fabric.api import *
from gearman import GearmanWorker


#Defining the host
host = ['localhost:4730']




def fun():
    print " this is a tes fun"





# Run the ssh task
#
def exe_job(worker, job):
    d = json.loads(job.data)
    env.host_string = d['host'] 
    cmd = d['command']
    retries = int(d['retries'])
    output = ""
    rc = -1

    # Run the fabric command. Do not abort on exit
    # Run job for the given number of retries
    tmp_retries = retries;
    while retries > 0:
        with settings(warn_only=True):
            result = run(cmd)
            output = output + str(result)

        if result.failed:
            if retries == 1:
                rc = -1
            else:
                next
        else:
            rc = 0
            break

        retries = retries - 1
    
    return json.dumps({ "rc": rc, "output": output })


#
# Main function
#
def main():
    print " this is the worker main function running .. ho haaa "
    gm_worker = gearman.GearmanWorker(host)
    gm_worker.register_task('exe_job',exe_job) 
    gm_worker.work()


if __name__ == '__main__':
    main()
