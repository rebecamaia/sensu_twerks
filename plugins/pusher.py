#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from sensu_plugin import SensuHandler

class PushedPusher(SensuHandler):
		def handle(self):
			client_name = self.event['client']['name']
			check_output = self.event['check']['output']
			app_key = "T7fjE1Kq8gX5TSVFF4hn"
			app_secret = "iPzm0cl38GdEHHZem1LLISCHt4aji1Pd90cA4nxCFb1ysSCpkA7PoCGz6ZvxrQhC"
			target_type = "app"
			content = "Alert from Sensu APP: %s: %s" % (client_name, check_output)
			payload = {'app_key':app_key,'app_secret':app_secret,'target_type':target_type,'content':content}
			url = "https://api.pushed.co/1/push"
			r = requests.post(url, data=payload)
			print(r.text)

PushedPusher()