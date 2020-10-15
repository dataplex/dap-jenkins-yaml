#!/usr/bin/env python3

class ConjurHost:
    def __init__(self, account, resource_type, name, api_key):
        self.__account = account
        self.__resource_type = resource_type
        self.__identity = name
        self.__api_key = api_key

    @property
    def account(self):
        return self.__account

    @property
    def name(self): 
        return self.__name

    @property
    def login_name(self):
        if self.__name.lower() == 'host/':
            return self.__name

        return 'host/' + self.__name

    @property
    def api_key(self):
        return self.__api_key