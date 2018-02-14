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

def send_data_influx(host, local, ds_name):
	payload = 'pool_max_size,host=%s value=%i' % (host, get_max_pool(local, ds_name))
	print payload
	url = 'http://sensu.esig.com.br:8086/write?db=java'
	r = requests.post(url,payload)
	print r
	payload = 'pool_current_size,host=%s value=%i' % (host, get_current_pool(local, ds_name))
	url = 'http://sensu.esig.com.br:8086/write?db=java'
	r = requests.post(url,payload)
	print r

def main():
	ds_name = sys.argv[1]
	local = sys.argv[2]
	host = get_client_name()

	send_data_influx(host, local, ds_name)

if __name__ == '__main__':
	main()
