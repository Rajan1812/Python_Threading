import threading
import time


def sleeper(n, name):
  print"{} sleeping for 5 minutes\n".format(name)
  time.sleep(n)
  print"{} woke up from sleep\n".format(name)


#t=threading.Thread( target = sleeper, name ='thread1', args= (5,'ram'))
#t.start()
#t.join()

thread_list=[]
start=time.time()
for i in range(5):
  t=threading.Thread(target=sleeper, name = 'thread' , args = (5,'t{}'.format(i)))
  thread_list.append(t)
  t.start()


for t in thread_list:
  t.join()

end = time.time()
print "total time = {}".format(end-start)
print "This is the main program"


