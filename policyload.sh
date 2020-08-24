#!/usr/bin/env bash

if [ "$#" != "6" ];then
    echo "Usage: $0 <url> <acct> <user:pass> <branch> <policy_file> <output_file>"
    exit 1
fi

URL=$1
ACCT=$2
CREDS=$3
POLICY_BRANCH=$4
POLICY_FILE=$5
POLICY_OUT=$6


# CUSER:CPASS can be provided by Jenkins OR loaded from CCP (preferred)
CUSER=$(echo $CREDS | cut -f1 -d: -)

# Login
api_key=$(curl -sk --user $CREDS https://$URL/authn/$ACCT/login)
if [ "$api_key" = "" ];then
   echo "Failure: Username/Password Incorrect"
   exit 1
fi

# Get Authentication Result
auth_result=$(curl -sk https://$URL/authn/$ACCT/$CUSER/authenticate -d "$api_key")
if [ "$auth_result" = "" ];then
  echo "Failure: Could not retrieve Auth Token with API Key"
  exit 1
fi

token=$(echo -n $auth_result | base64 | tr -d '\r\n')

AUTH_TOKEN="Authorization: Token token=\"$token\""

url="https://$URL/policies/$ACCT/policy/$POLICY_BRANCH"
curl -s -k -H "$AUTH_TOKEN" \
  -X PUT \
  -d "$(< $POLICY_FILE )" \
  $url > $POLICY_OUT

cat $POLICY_OUT
