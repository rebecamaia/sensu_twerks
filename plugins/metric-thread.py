import requests
import json
import sys

def get_client_name():
	client_path = "/etc/sensu/conf.d/client.json"
	data = json.load(open(client_path))
	return data['client']['name']

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
	local = sys.argv[1]
	param = sys.argv[2]
	host = get_client_name()

	if param == "maxThreads":
		print ("%s %s %s") % (host, param, get_max_threads(local))
	elif param == "currentThreadsCount":
		print ("%s %s %s") % (host, param, get_current_threads_busy(local))

if __name__ == '__main__':
	main()
