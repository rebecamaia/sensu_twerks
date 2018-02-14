import requests
import sys
import json
import subprocess

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

	warn_param = 80
	crit_param = 90

	current_pool_percentage = ((get_current_pool(local,ds_name)*100)/get_max_pool(local,ds_name))

	if current_pool_percentage < warn_param:
		print "OK: pool count is under %i %% - Current: %i %%" % (warn_param, current_pool_percentage)
		sys.exit(0)
	elif current_pool_percentage >= warn_param:
		print "WARNING: pool count is over %i %% - Current: %i %%" % (warn_param, current_pool_percentage)
		sys.exit(0)
	elif current_pool_percentage >= crit_param:
		print "CRITICAL: pool count is over %i %% - Current: %i %%" % (warn_param, current_pool_percentage)
		sys.exit(0)


if __name__ == '__main__':
	main()
