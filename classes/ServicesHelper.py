#!/usr/bin/env python

import sys
import requests
import json

class ServicesHelper:
    def __init__(self, dap_host, pas_host, ccp_query, verifySsl=True):
        self.dap_host = dap_host
        self.pas_host = pas_host
        self.verifySsl = verifySsl

    def dap_info():
        url = 'https://' + dap_host + '/info'
        return requests.get(url, verify=False).json()

    def pas_rest_creds():
        r = requests.get(ccp_query, verify=self.verifySsl)
        return r.json()

