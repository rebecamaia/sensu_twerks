import requests
import json
import sys

def get_max_threads(local):
	param = "maxThreads"
	addr = ("http://%s/jolokia/read/jboss.web:type=ThreadPool,name=ajp-0.0.0.0-8009/%s") % (local, param)
	req = requests.get(addr)
	return req.json()['value']

def get_current_threads(local):
	param = "currentThreadsCount"
	addr = ("http://%s/jolokia/read/jboss.web:type=ThreadPool,name=ajp-0.0.0.0-8009/%s") % (local, param)
	req = requests.get(addr)
	return req.json()['value']

def get_current_threads_busy(local):
	param = "currentThreadsBusy"
	addr = ("http://%s/jolokia/read/jboss.web:type=ThreadPool,name=ajp-0.0.0.0-8009/%s") % (local, param)
	req = requests.get(addr)
	return req.json()['value']


def main():
	#local = "127.0.0.1"
	param = sys.argv[1] #param
	local = sys.argv[2] #local

	max_threads = get_max_threads(local)
	warn_param = 80
	crit_param = 90

	if (param == "currentThreadsBusy"):
		busy_thread_percentage = ((get_current_threads_busy(local)*100)/get_max_threads(local))


		if busy_thread_percentage < warn_param:
			print "OK: Thread Busy Count under %i %% - Current: %i %%" % (warn_param, busy_thread_percentage)
			sys.exit(0)
		elif busy_thread_percentage >= warn_param:
			print "OK: Thread Busy Count over %i %% - Current: %i %%" % (warn_param, busy_thread_percentage)
			sys.exit(1)
		elif busy_thread_percentage >= crit_param:
			print "OK: Thread Busy Count under %i %% - Current: %i %%" % (crit_param, busy_thread_percentage)
			sys.exit(2)


if __name__ == '__main__':
	main()
