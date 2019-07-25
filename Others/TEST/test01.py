import commands
result=commands.getoutput("sudo i2cdetect -y 1")
print result
