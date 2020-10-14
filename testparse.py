#!/usr/bin/env python3

import sys
import json

def main(argv):
    policy_path = argv[0]
    account = argv[1]

    username = 'testusername'
    password = 'testpass'
    cred_t = (username, password)
    auth_body = '{ "username": "%s", "password": "%s" }' % cred_t

    print(f'{auth_body}')
    print(f'Reading file...{policy_path}')

    dap_hosts = {}
    with open(policy_path) as f:
         policy_output = f.read()
         policy_json = json.loads(policy_output)
         for created_role in policy_json["created_roles"]:
             crole = policy_json["created_roles"][created_role]
             crid = crole["id"].replace(f'{account}:host:', '')
             api_key = crole["api_key"]
             dap_hosts[crid] = api_key

    for key in dap_hosts:
        print(f'{key} - {dap_hosts[key]}')

if __name__ == "__main__":
   main(sys.argv[1:])
