#!/usr/bin/env python3

import sys
import requests
import json

class DAPPolicyDeploymentHelper:
    def __init__(self, servicesHelper):
        self.__servicesHelper = servicesHelper

    def onboard_hosts(self):
        account = self.dap_info_account()
        policy_out_json = self.__servicesHelper.policy_output_json()

        hosts_to_onboard = parse_hosts(policy_out_json, account) 

        if hosts_to_onboard.len() > 0:
            pas_auth = pas_rest_authenticate()
            for dap_host in hosts_to_onboard:
                self.__serviceHelper.onboard_host(account, dap_host, hosts_to_onboard[dap_host])

    def parse_hosts(self, policy_out_json, account):
        dap_hosts = {}
        with open(policy_path) as f:
            policy_output = f.read()
            policy_json = json.loads(policy_output)
            for created_role in policy_json["created_roles"]:
                crole = policy_json["created_roles"][created_role]
                crid = crole["id"].replace(f'{account}:host:', '')
                api_key = crole["api_key"]
                dap_hosts[crid] = api_key
        return dap_hosts

    def pas_host_factory(self, account, dap_host, api_key):
        

    def dap_info_account(self):
        info_json = self.__servicesHelper.dap_info()
        return info_json['configuration']['conjur']['account']

    def pas_rest_authenticate(self, auth_body):
        ccp_result = self.__servicesHelper.pas_rest_credentials()
        auth_body = '{ "username": "%s", "password": "%s" }' % ccp_result
        return self.__servicesHelper.pas_rest_authenticate(auth_body)
