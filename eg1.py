from multiprocessing import Process
import os
import time

def run_proc(name):
    print '##1 - Run child process' + name
    time.sleep(10)
    print '##2 - Run child process' + name

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    print "#1 parent process before sleep"
    for i in range(10000000):
        a = 0
    print "#2 parent process before sleep"
    time.sleep(1)
    print "#3 parent process after sleep"
    #p.join()
    print 'after join'
