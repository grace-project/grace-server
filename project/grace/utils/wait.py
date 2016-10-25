import os
import time
import socket


def wait_for_db(timeout_attempts=30):
	"""
	Blocking call until database service is available.
	"""
	host_port = (os.environ["DB_HOST"], int(os.environ["DB_PORT"]))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	while 1 and timeout_attempts > 0:
		try:
			sock.connect(host_port)
			sock.close()
			time.sleep(1)
			break
		except:
			timeout_attempts -= 1
			time.sleep(0.25)