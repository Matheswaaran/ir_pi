import time
from threading import Timer
def print_time():
                print "From print_time",time.time()

def print_some_times():
                      print_time.time()
                      Timer(5, print_time, ()).start()
                      Timer(10, print_time,()).start()
                      time.sleep(11)
                      print time.time()


                      print some_
                       
