import subprocess
import sys

from sensu_plugin import SensuHandler

class JBossFixer(SensuHandler):
        def handle(self):
                target_client = self.event['client']['name']
                check_command = self.event['check']['command']
                inst = check_command.split()[1]
                cmd = " \'/usr/bin/jboss -r " + inst + "\'"
                ssh = "ssh sistemas@" + target_client +  cmd
                res = subprocess.check_output(ssh, shell=True)
                print(res)

JBossFixer()
