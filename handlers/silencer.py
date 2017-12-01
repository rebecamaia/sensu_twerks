#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sensu_plugin import SensuHandler

import json
import subprocess
import sys

class SilencerHandler(SensuHandler):
	def handle(self):
		#receiving check output from sensu handler
		target_client = self.event['client']['name']
		sensu_cli = "/opt/sensu/embedded/bin/sensu-cli "
		cmd = sensu_cli + "event list -f json"
		res = subprocess.check_output(cmd.split())
		dic_event_list = json.loads(res)

		for i in range(len(dic_event_list)):
			if 'http' in dic_event_list[i]['check']['name']:
				cmd = sensu_cli + "silenced create -f -c " + dic_event_list[i]['check']['name'] + " -n client:" + target_client + " -r \"Dependency_Check_VPN\""
				res = subprocess.check_output(cmd.split())
				print(res)

SilencerHandler()