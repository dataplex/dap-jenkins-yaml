#!/usr/bin/env bash

# <DAP_Host Example>
# dapmaster.dpxlab.net
# </DAP_Host Example>
#
# <CCP_Info Example>
# https://pvwa.dpxlab.net/AIMWebService/api/Accounts?AppID=DAP_Jenkins_Pipeline&Safe=DAP_API_Connectors&Folder=Root&Object=DAP_API_Connector
# </CCP_Info Example>
#
# <REST_API_HOST Example>
# pvwa.example.com
# </REST_API_HOST Example>

if [[ $# -lt 4 ]];then
	echo "Usage: $0 "DAP_Host" "CCP_Info" "REST_API_HOST" "./path/to/policy-load.out""
	echo " -- See script source for example input format -- "
	exit 1
fi

DEBUG=1

#DAP_HOST="master.dpxlab.net"
#CCP_QUERY_URI="https://pvwa.dpxlab.net/AIMWebService/api/Accounts?AppID=DAP_Jenkins_Pipeline&Safe=DAP_API_Connectors&Folder=Root&Object=DAP_API_Connector"
#REST_API_HOST="pvwa.dpxlab.net"
#POLICY_OUT_PATH="./output/policy-load.out"
DAP_HOST="$1"
CCP_QUERY_URI="$2"
REST_API_HOST="$3"
POLICY_OUT_PATH="$4"

function debug_msg {
    if [ "$DEBUG" = "1" ]; then
        echo "$1"
    fi
}

REST_API_USER=""
REST_API_PASS=""
function get_rest_credentials_from_ccp {
    local ccp_response
    local curl_exit_code
    ccp_response="$(curl -sk $CCP_QUERY_URI)" curl_exit_code=$?
    if [ "$curl_exit_code" != "0" ]; then
	    debug_msg "$curl_exit_code - CCP Resp: $ccp_response"
	    exit 1
    fi

    REST_API_PASS="$(echo "$ccp_response" | tr '",' '"\n' | grep Content | sed "s/.*Content\":\"//g" | sed "s/\"$//g")"
    REST_API_USER="$(echo "$ccp_response" | tr '",' '"\n' | grep UserName | sed "s/.*UserName\":\"//g"  | sed "s/\"$//g")"
    debug_msg "API User: $REST_API_USER   --- API PASS: $REST_API_PASS"
}

REST_AUTH_TOKEN=""
function authenticate_to_rest_api {
    local rest_cyberark_logon_uri
    local rest_auth_body
    rest_cyberark_logon_uri="https://$REST_API_HOST/PasswordVault/API/auth/Cyberark/Logon"
    rest_auth_body="{\"username\":\"$REST_API_USER\",\"password\":\"$REST_API_PASS\"}"

    REST_AUTH_TOKEN="$(curl -sk -X POST -H "Content-Type: application/json" -d"$rest_auth_body" $rest_cyberark_logon_uri)"
    debug_msg "$REST_AUTH_TOKEN"
}

function create_add_account_body {
	local a_name=$1
	local address=$2
	local username=$3
	local api_key=$4
	local conjurAccount=$5
	local safeName=$6

	local platformId="ConjurHost"
	local secretType="key"

echo "{
  \"name\": \"$a_name\",
  \"address\": \"$address\",
  \"userName\": \"$username\",
  \"platformId\": \"$platformId\",
  \"safeName\": \"$safeName\",
  \"secretType\": \"password\",
  \"secret\": \"$api_key\",
  \"platformAccountProperties\": {
      \"ConjurAccount\": \"$conjurAccount\"
   },
  \"secretManagement\": {
    \"automaticManagementEnabled\": true
  }
}"
}

function onboard_host_account {
	local account="$1"
	local hostid="$2"
	local api_key="$3"

	local rest_add_account_uri="https://$REST_API_HOST/PasswordVault/API/Account"
	debug_msg "Creating: $account - $hostid - $api_key"
	local rest_add_body
	rest_add_body="$(create_add_account_body "$account_$hostid" "https://$DAP_HOST/api" "host/$hostid" "$api_key" "$account" "$hostid")"

	debug_msg "REST Body: $rest_add_body"
    curl -svk -X POST -H "Authorization: $REST_AUTH_TOKEN" -H "Content-Type: application/json" -d"$rest_add_body" $rest_add_account_uri
}


function process_policy_load_for_hosts {
	local dap_account
	dap_account="$(cat $POLICY_OUT_PATH | grep "host.*{$" | cut -f1 -d: | uniq | sed "s/^ .*\"//g")"
	debug_msg "DAP ACCOUNT: $dap_account"

	readarray -t hosts_arr <<<"$(cat $POLICY_OUT_PATH | grep "id.*host" | cut -f4 -d: | sed "s/\",//g")"

	for chost in "${hosts_arr[@]}";do
		debug_msg "Looping $chost"
		api_key="$(cat $POLICY_OUT_PATH | grep -A1 "id.*dev:host:$chost" | \
			grep api_key | cut -f2 -d: | sed "s/[ \"]//g")"

		onboard_host_account "$dap_account" "$chost" "$api_key"
	done
}

function main {
    debug_msg "CCP Query: $CCP_QUERY_URI"
    get_rest_credentials_from_ccp
    authenticate_to_rest_api
    process_policy_load_for_hosts
}

main "$@"
