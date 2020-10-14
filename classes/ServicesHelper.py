#!/usr/bin/env python

import requests
import json

class ServicesHelper:
    def __init__(self, config, ccp_query, policy_out_path, verifySsl=True):
        self.dap_host = dap_host
        self.pas_host = pas_host
        self.ccp_query = ccp_query
        self.policy_out_path = policy_out_path
        self.verifySsl = verifySsl

    def dap_info(self):
        url = 'https://' + self.dap_host + '/info'
        return requests.get(url, verify=self.verifySsl).json()

    def pas_rest_credentials(self):
        r = requests.get(self.ccp_query, verify=self.verifySsl)
        resp_json = r.json()
        username = resp_json["UserName"]
        password = resp_json["Content"]
        return (username, password)

    def pas_rest_authenticate(self, auth_body):
        url = "https://%s/PasswordVault/API/auth/Cyberark/Logon" % (self.pas_host)
        headers = { "Content-Type": "application/json" }
        response = requests.post(url, data=auth_body, headers=headers, verify=self.verifySsl)
        return response.json()["CyberArkLogonResult"]

    def policy_output_json(self):
       with open(policy_out_path) as f:
           return f.read()

    def onboard_host(self, account, identity, apikey, safename, ):
        # platform_id = ConjurHostDev

    def build_platform_body(self, objectname account, identity, apikey, safename, platform_id):
        data = {}
        data['name'] = objectname
        data['address'] = self.dap_host
        data['userName'] = identity
        data['platformId'] = platform_id
        data['safeName'] = safename
        data['secretType'] = 'password'
        data['secret'] = apikey
        platformAccountProperties = {}
        platformAccountProperties['ConjurAccount'] = account
        secretManagement = {}
        secretManagement['automaticManagementEnabled'] = True
        data['platformAccountProperties'] = platformAccountProperties
        data['secretManagement'] = secretManagement
        return json.dumps(data)