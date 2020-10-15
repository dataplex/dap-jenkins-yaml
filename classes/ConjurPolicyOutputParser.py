#!/usr/bin/env python3

class ConjurPolicyOutputParser:
    def hosts(self, policy_output):
        dap_hosts = []
        policy_json = json.loads(policy_output)
        for created_role in policy_json["created_roles"]:
            crole = policy_json["created_roles"][created_role]
            api_key = crole["api_key"]

            crolesplit = crole["id"].split()
            cr_acct = crolesplit[0]
            cr_type = crolesplit[1]
            cr_name = crolesplit[2]

            dap_hosts.append(ConjurHost(cr_acct, cr_type, cr_name, api_key))
        return dap_hosts