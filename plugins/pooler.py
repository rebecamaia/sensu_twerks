import requests
import json

from sensu_plugin import SensuHandler

class Pooler(SensuHandler):
        def handle(self):
                target_client = self.event['client']['name']
                check_output = self.event['check']['output']
                ds_name = self.event['check']['name'].split("-")[3]
                result = check_output.split(" ")[2]

                if check_output.split(" ")[1] == "MaxSize":
                        param = "pool-max-size"
                elif check_output.split(" ")[1] == "ConnectionCount":
                        param = "pool-current-connections"

                payload = '%s-%s,host=%s value=%s' % (param, ds_name, target_client, result)
                print payload
                url = 'http://sensu.esig.com.br:8086/write?db=java'
                r = requests.post(url,payload)
                print(r)

Pooler()
