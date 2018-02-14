import requests
import json

from sensu_plugin import SensuHandler

class InfluxFeeder(SensuHandler):
    def handle(self):
        target_client = self.event['client']['name']
        check_result = self.event['check']['status']
        payload = 'vpn-traffic,host=%s value=%s' % (target_client,check_result)
        url = 'http://sensu.esig.com.br:8086/write?db=grafana'
        r = requests.post(url,payload)
        print(r)

InfluxFeeder()