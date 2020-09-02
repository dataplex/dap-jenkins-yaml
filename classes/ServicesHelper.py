#!/usr/bin/env python

import requests
import json

class ServicesHelper:
    def __init__(self, dap_host, pas_host, ccp_query, verifySsl=True):
        self.dap_host = dap_host
        self.pas_host = pas_host
        self.verifySsl = verifySsl

    def dap_info(self):
        url = 'https://' + self.dap_host + '/info'
        return requests.get(url, verify=self.verifySsl).json()

    def pas_rest_credentials(self):
        r = requests.get(ccp_query, verify=self.verifySsl)
        return r.json()

