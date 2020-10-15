#!/usr/bin/env python3

import sys
import requests
import json

import ConjurPolicyOutputParser

class DAPPolicyDeploymentHelper:
    def __init__(self, servicesHelper, policyOutputParser):
        self.__servicesHelper = servicesHelper
        self.__policyOutputParser = policyOutputParser

    def onboard_hosts(self):
        policy_out = self.__servicesHelper.policy_output_raw()
        hosts_to_onboard = self.__policyOutputParser.hosts(policy_out)
        self.__servicesHelper.onboard_hosts(hosts_to_onboard)

