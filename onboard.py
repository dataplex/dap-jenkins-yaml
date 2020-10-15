#!/usr/bin/env python3

import sys
import configparser

from classes.ServicesHelper import ServicesHelper
from classes.DAPPolicyDeploymentHelper import DAPPolicyDeploymentHelper
from classes.OnboardingConfig import OnboardingConfig

def main(argv):
    config_file = argv[0]
    config_env = argv[1]

    ccp_query = argv[2]
    policy_out_path = argv[3]

    cp = configparser.ConfigParser()
    cp.read(config_file)

    config = OnboardingConfig(cp[config_env], ccp_query, policy_out_path)
    svchelper = ServicesHelper(config)
    deployHelper = DAPPolicyDeploymentHelper(svchelper)

    deployHelper.onboard_hosts()

if __name__ == "__main__":
   main(sys.argv[1:])
