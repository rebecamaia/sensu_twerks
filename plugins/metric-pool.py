import requests
import sys
import json
import subprocess

def get_client_name():
	client_path = "/etc/sensu/conf.d/client.json"
	data = json.load(open(client_path))
	return data['client']['name']

def get_max_pool(local, ds_name):
	param = "MaxSize"
	addr = ("http://%s/jolokia/read/jboss.jca:*,service=ManagedConnectionPool/%s") % (local, param)
	try:
		req = requests.get(addr)
		json_key = "jboss.jca:name=jdbc/%s,service=ManagedConnectionPool" % ds_name
		res = req.json()['value'][json_key][param]
	except LookupError:
		print "DB Not Found"
		return sys.exit(3)

	return res

def get_current_pool(local, ds_name):
	param = "ConnectionCount"
	addr = ("http://%s/jolokia/read/jboss.jca:*,service=ManagedConnectionPool/%s") % (local, param)
	try:
		req = requests.get(addr)
		json_key = "jboss.jca:name=jdbc/%s,service=ManagedConnectionPool" % ds_name
		res = req.json()['value'][json_key][param]
	except LookupError:
		print "DB Not Found"
		return sys.exit(3)

	return res

def main():
	ds_name = sys.argv[1]
	local = sys.argv[2]
	param = sys.argv[3]
	host = get_client_name()

	if param == "MaxSize":
		print ("%s %s %s") % (host, param, get_max_pool(local,ds_name))
	elif param == "ConnectionCount":
		print ("%s %s %s") % (host, param, get_current_pool(local,ds_name))

if __name__ == '__main__':
	main()
