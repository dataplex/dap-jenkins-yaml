#!/usr/bin/env python3

import sys

from classes.ServicesHelper import ServicesHelper
from classes.DAPPolicyDeploymentHelper import DAPPolicyDeploymentHelper

def main(argv):
    config_file = argv[0]
    ccp_query = argv[1]
    policy_out_path = argv[3]

    config = OnboardingConfig.parse(config_file)
    svchelper = ServicesHelper(config, ccp_query, policy_out_path, False)
    deployHelper = DAPPolicyDeploymentHelper(svchelper)

    deployHelper.onboard_hosts()

if __name__ == "__main__":
   main(sys.argv[1:])
