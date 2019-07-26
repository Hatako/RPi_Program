import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG2 = 24				# set dir2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
print("please wait")
sleep(1)				# delay for 5 seconds
print("go")
p1 = GPIO.PWM(AN1, 100)			# set pwm for M1
p2 = GPIO.PWM(AN2, 100)			# set pwm for M2

p1.start(0)
p2.start(0)

try:					
  while True:

   print ("左")				# display "Forward" when programe run
   GPIO.output(DIG1, GPIO.HIGH)		# set DIG1 as HIGH, M1B will turn ON
   GPIO.output(DIG2, GPIO.LOW)		# set DIG2 as HIGH, M2B will turn ON
   p1.start(20)			# set speed for M1 at 100%
   p2.start(20)			# set speed for M2 at 100%
   sleep(5)				#delay for 2 second

   print ("後退")
   GPIO.output(DIG1, GPIO.LOW)          # set DIG1 as LOW, to control direction
   GPIO.output(DIG2, GPIO.LOW)          # set DIG2 as LOW, to control direction
   p1.start(20)                        # set speed for M1 at 100%
   p2.start(20)                        # set speed for M2 at 100%
   sleep(5)                             #delay for 2 second

   print("前進")
   GPIO.output(DIG1, GPIO.HIGH)         # set DIG1 as HIGH, to control direction
   GPIO.output(DIG2, GPIO.HIGH)         # set DIG2 as HIGH, to control direction
   p1.start(20)                        # set speed for M1 at 100%
   p2.start(20)                        # set speed for M2 at 100%
   sleep(5)                             #delay for 2 second

   print ("右")
   GPIO.output(DIG1, GPIO.LOW)
   GPIO.output(DIG2, GPIO.HIGH)
   p1.start(20)
   p2.start(20)
   sleep(5)


except:					# exit programe when keyboard interupt
   p1.start(0)				# set speed to 0
   p2.start(0)				# set speed to 0
					# Control+x to save file and exit