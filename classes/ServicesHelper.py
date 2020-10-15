#!/usr/bin/env python

import requests
import json

class ServicesHelper:
    def __init__(self, config):
        self.__config = config

    def policy_output_raw(self):
       with open(self.__config.policy_out_path) as f:
           return f.read()

    def onboard_hosts(self, hosts_to_onboard):
        if hosts_to_onboard.len() == 0:
            return

        url = f'https://{self.__config.pam_host}/PasswordVault/API/Account'
        auth_header = pas_rest_authenticate()
        headers = { "Content-Type": "application/json", "Authorization": auth_header }

        for conjur_host in hosts_to_onboard:
            add_body = AddConjurHostRequestBuilder(self.__config, conjur_host).build()
            response = requests.post(url, headers=headers, data=add_body, verify=self.__config.verifySsl)
            print(response)

    def pas_rest_authenticate(self):
        url = f"https://{self.__config.pam_host}/PasswordVault/API/auth/Cyberark/Logon"

        ccp_result = pas_rest_credentials()
        auth_body = '{ "username": "%s", "password": "%s" }' % ccp_result
        headers = { "Content-Type": "application/json" }

        response = requests.post(url, data=auth_body, headers=headers, verify=self.__config.verifySsl)
        return response.json()["CyberArkLogonResult"]

    def pas_rest_credentials(self):
        r = requests.get(self.__config.ccp_query, verify=self.__config.verifySsl)
        resp_json = r.json()
        username = resp_json["UserName"]
        password = resp_json["Content"]
        return (username, password)
