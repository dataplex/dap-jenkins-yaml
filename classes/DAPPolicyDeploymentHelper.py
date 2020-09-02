#!/usr/bin/env python

import sys
import requests
import json

class DAPPolicyDeploymentHelper:
    def __init__(self, servicesHelper):
        self.__servicesHelper = servicesHelper

    def dap_info_account(self):
        info_json = self.__servicesHelper.dap_info()
        return info_json['configuration']['conjur']['account']

    def pas_rest_credentials():
        ccp_result = __servicesHelper.pas_rest_creds()
        username = ccp_result['Content']
        password = ccp_result['UserName']
        return (username, password)

    def create_pas_auth_body(credentials):
        return '{ "username": "%s", "password": "%s" }' % credentials

    def pas_rest_authenticate(rest_api_host, auth_body):
        url = "https://%s/PasswordVault/API/auth/Cyberark/Logon" % (rest_api_host)
        return requests.post(url, data=auth_body, verify=False).text
