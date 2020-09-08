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

    def pas_rest_credentials(self):
        ccp_result = self.__servicesHelper.pas_rest_credentials()
        username = ccp_result['Content']
        password = ccp_result['UserName']
        return (password, username)

    def create_pas_auth_body(self, credentials):
        return '{ "username": "%s", "password": "%s" }' % credentials

    def pas_rest_authenticate(self, auth_body):
        result = self.__servicesHelper.pas_rest_authenticate(auth_body)
        return result.text
