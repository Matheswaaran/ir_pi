import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)                            #Right sensor connection
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left sensor connection
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
while True:
          i=GPIO.input(3)                         #Reading output of right IR sensor
          j=GPIO.input(16)
          time.sleep(3)
      
          if i== 1:                                 #Right IR sensor detects a0n object               
                  print "Obstacle detected on A",
                  time.sleep(5)           
                  if j==1:                              #Left IR sensor detects an object
                         
                        print "Obstacle detected on B",
                        time.sleep(1)
                        GPIO.output(8,GPIO.HIGH)
                        time.sleep(2)
                        GPIO.output(8,GPIO.LOW)
                        break

                  else:
                     print "obstacle not detected on B",
                     GPIO.output(7,GPIO.HIGH)
                     GPIO.output(11,GPIO.HIGH)
                     time.sleep(2)
                     GPIO.output(7,GPIO.LOW)
                     GPIO.output(11,GPIO.LOW)
                     break
          else:
              print "obstacle not detected on a",
              GPIO.output(7,GPIO.HIGH)
              GPIO.output(11,GPIO.HIGH)
              time.sleep(2)	
              GPIO.output(7,GPIO.LOW)
              GPIO.output(11,GPIO.LOW)	
   
              break

