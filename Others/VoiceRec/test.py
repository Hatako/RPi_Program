# coding:utf-8
import subprocess
import socket
import time

def main():
	p = subprocess.Popen("./run-dnn-mod.sh", stdout=subprocess.PIPE, shell=True)
	print('Initiating')
	time.sleep(5)
	print('Done')
	pid = str(p.pid)

	host = 'localhost'
	port = 10500

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))

	while True:
		try:
			data = client.recv(1024).decode("utf-8")
			if len(data) > 1:
				print(data)
		except KeyboardInterrupt:
			print ("KeyboardInterrupt occured.")
			p.kill()
			subprocess.call("kill " + pid, shell=True)
			client.close()
			quit()

if __name__ == "__main__":
	main()
