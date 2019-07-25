#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
# ===========================================================================
# Example Code
# ===========================================================================
# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 100 # Min pulse length out of 4096
servoMax = 515   # Max pulse length out of 4096

#def setServoPulse(channel, pulse):
 # pulseLength = 1000000                   # 1,000,000 us per second
  #pulseLength /= 60                       # 60 Hz
  #print "%d us per period" % pulseLength
  #pulseLength /= 4096                     # 12 bits of resolution
  #print "%d us per bit" % pulseLength
  #pulse *= 1000
  #pulse /= pulseLength
  #pwm.setPWM(channel, 0, pulse)



pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
pwm.setPWM(0,0,servoMin)
time.sleep(1)


def servo(inter, channel):
	for i in range(servoMin,servoMax+1):
		pwm.setPWM(channel,0,i)		
		iRange=servoMax-servoMin
		angle=180.0*(i-100)/iRange
		print('angle: {0:.1f} [degree]'.format(angle))	
		time.sleep(inter)
	time.sleep(1)
	for i in range(servoMin,servoMax+1):
		duty=servoMax+servoMin-i
		pwm.setPWM(channel,0,duty)		
#		iRange=servoMax-servoMin
#		angle=180.0*(i-100)/iRange
#		print('angle: {0:.1f} [degree]'.format(angle))	
		print(duty)
		time.sleep(inter)
	time.sleep(1)

for i in range(5,11):
	servo(0.001*i,0)


#while (True):
  # Change speed of continuous servo on channel O
 # pwm.setPWM(0, 0, servoMin)
  #time.sleep(1)
  #pwm.setPWM(0, 0, servoMax)
  #time.sleep(1)



