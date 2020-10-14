#!/usr/bin/env python3

import json

objectname = 'test_object_something'
dap_host = 'uatdapmaster.test.com'
identity = 'host/test_object_something'
platform_id = 'ConjurHostDev'
safename = 'test_object_something'
apikey = 'asdfagfaadfgbvfabcfvasdrfawefevvacdsfsafsdfe'
account = 'uatdap'

data = {}
data['name'] = objectname
data['address'] = dap_host
data['userName'] = identity
data['platformId'] = platform_id
data['safeName'] = safename
data['secretType'] = 'password'
data['secret'] = apikey
platformAccountProperties = {}
platformAccountProperties['ConjurAccount'] = account
secretManagement = {}
secretManagement['automaticManagementEnabled'] = True
data['platformAccountProperties'] = platformAccountProperties
data['secretManagement'] = secretManagement

json_dump = json.dumps(data)

print(json_dump)
