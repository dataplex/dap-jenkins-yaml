#!/usr/bin/env python3

import configparser

class OnboardingConfig:
    @staticmethod
    def parse(self, configfile):
       config = configparser.ConfigParser().read(configfile)
       onboardconfig = new OnboardingConfig(config)
       return onboardingconfig

    def __init__(self, config):
        self.verifySsl = config['DEFAULT']['verifySsl']
        self.__account = config['DEFAULT']['account']
        self.__masterhost = config['DEFAULT']['masterhost']
        self.__followerhost = config['DEFAULT']['followerhost']
        self.__pamhost = config['DEFAULT']['pamhost']
        self.__platform_id = config['PlatformSettings']['platform_id']
        self.__automgmtenabled = config['PlatformSettings']['automaticManagementEnabled']

    @property
    def verifySsl(self):
        return self.__verifySsl

    @verifySsl.setter
    def verifySsl(self, var):
        if var == 'yes'
            self.__verifySsl = True
        else
            self.__verifySsl = False

    @property
    def account(self):
        return self.__account

    @property
    def masterhost(self):
        return self.__masterhost

    @property
    def followerhost(self):
        return self.__followerhost

    @property
    def pamhost(self):
        return self.__pamhost

    @property
    def platform_id(self):
        return self.__platform_id

    @property
    def automatic_management_enabled(self):
        return self.__automgmtenabled