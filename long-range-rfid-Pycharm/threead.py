# import time
# from threading import Thread
#
# def sleeper(i):
#     print "thread %d sleeps for 5 seconds" % i
#     time.sleep(5)
#     print "thread %d woke up" % i
#
# for i in range(10):
#     t = Thread(target=sleeper, args=(i,))
#     t.start()
#
# # ------------------------------------------------------------------------------------------------
#
# def post(epc,temp,tid):
#     import requests
#     userdata = {"epc": epc, "temp": temp, "tid": tid}
#     resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php',params=userdata)
#     print(resp.content)


import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass