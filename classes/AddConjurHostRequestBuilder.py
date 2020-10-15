#!/usr/bin/env python3

class AddConjurHostRequestBuilder:
    def __init__(self, config, host_to_add):
        self.__config = config
        self.__host = host_to_add

    def build(self):
        data = {}
        data['secretType'] = 'password'

        data['safeName'] = self.__host.name
        data['name'] = "host-" + self.__host.name
        data['userName'] = self.__host.login_name
        data['secret'] = self.__host.api_key

        data['address'] = self.__config.dap_master
        data['platformId'] = self.__config.platform_id

        platformAccountProperties = {}
        platformAccountProperties['ConjurAccount'] = self.__host.account
        data['platformAccountProperties'] = platformAccountProperties

        secretManagement = {}
        secretManagement['automaticManagementEnabled'] = self.__config.automatic_management_enabled
        data['secretManagement'] = secretManagement

        return json.dumps(data)