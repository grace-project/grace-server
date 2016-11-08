import os
import time
import psycopg2


def wait_for_db(timeout_attempts=30):
	"""
	Blocking call until database service is available.
	"""
	_ = os.environ
	login = "host='%s' port='%s' dbname='%s' user='%s' password='%s'" % (
		_["DB_HOST"], _["DB_PORT"], _["DB_NAME"], _["DB_USER"], _["DB_PASS"]
	)

	while 1 and timeout_attempts > 0:
		try:
			conn = psycopg2.connect(login)
			conn.close()
			break
		except:
			timeout_attempts -= 1
			time.sleep(0.25)