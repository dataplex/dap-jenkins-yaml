#!/usr/bin/env python3

import sys
import configparser
from classes.OnboardingConfig import OnboardingConfig

def main(argv):
    configfile = argv[0]
    configenv = argv[1]

    cp = configparser.ConfigParser()
    cp.read(configfile)
    config = OnboardingConfig(cp[configenv])

    print(f'Account: {config.account}')
    print(f'DAP Host: {config.dap_host}')
    print(f'PAM Host: {config.pam_host}')

if __name__ == "__main__":
   main(sys.argv[1:])
