#!/usr/bin/env python

import requests
import json

class ServicesHelper:
    def __init__(self, dap_host, pas_host, ccp_query, verifySsl=True):
        self.dap_host = dap_host
        self.pas_host = pas_host
        self.ccp_query = ccp_query
        self.verifySsl = verifySsl

    def dap_info(self):
        url = 'https://' + self.dap_host + '/info'
        return requests.get(url, verify=self.verifySsl).json()

    def pas_rest_credentials(self):
        r = requests.get(self.ccp_query, verify=self.verifySsl)
        return r.json()

    def pas_rest_authenticate(self, auth_body):
        url = "https://%s/PasswordVault/API/auth/Cyberark/Logon" % (self.pas_host)
        print url, auth_body
        response = requests.post(url, data=auth_body, verify=self.verifySsl)
        print response
        return response.text

