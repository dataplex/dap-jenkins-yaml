#!/usr/bin/env python

from classes.ServicesHelper import ServicesHelper
from classes.DAPPolicyDeploymentHelper import DAPPolicyDeploymentHelper

def main(argv):
    dap_host = argv[0]
    ccp_query = argv[1]
    rest_api_host = argv[2]
    policy_out_path = argv[3]

    svchelper = ServicesHelper(dap_host, rest_api_host, ccp_query)
    deployHelper = DAPPolicyDeploymentHelper(svchelper)

    # pas_auth_header = deployHelper.pas_rest_authenticate(deployHelper.create_pas_auth_body(deployHelper.pas_rest_credentials()))

    print 'DAP host: ', dap_host
    print 'CCP Query: ', ccp_query
    print 'REST API: ', rest_api_host
    print 'Policy File: ', policy_out_path

if __name__ == "__main__":
   main(sys.argv[1:])
