##
import RPi.GPIO as GPIO
import time,threading,sys
from threading import Timer
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def periodicUpdate():
          while True:
                i=GPIO.input(3)
                j=GPIO.input(16)
                exittimer=threading.Timer(3.0,_exit)
                exittimer.start()
          

                if i==1:
                       print "obstacle detected on a",
                       exittimer=threading.Timer(3.0,_exit1)
                       exittimer.start()
                                            
                       if j==1:
                              print "obstacle detected on b",
                              break

                 
                 
                 
          
          
def _exit():                
          print "obstacle not detected on a",
          sys.exit()
def _exit1():
            print "obstacle not detected on b",
           
            sys.exit()
periodicUpdate()
