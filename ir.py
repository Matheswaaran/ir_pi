
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)                            #Right sensor connection

while True:
          i=GPIO.input(3)                         #Reading output of right IR sensor
        
          if i==1:                                #Right IR sensor detects an object
               print "Obstacle detected ",
               break  
              
