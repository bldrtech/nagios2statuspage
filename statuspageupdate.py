#!/usr/bin/python3
import requests
import argparse

# Get required values from arguments
parser=argparse.ArgumentParser()
parser.add_argument('api_key',help="Enter an provider api_key")
parser.add_argument('page_id',help="Enter the page_id to update")
parser.add_argument('comp_id',help="Enter the component id to update")
parser.add_argument('state',help="Enter the monitored state")
args=parser.parse_args()
api_key=args.api_key
page_id=args.page_id
comp_id=args.comp_id
state=args.state

# Set api url and headers
url="https://api.statuspage.io/v1/pages/"
headers={"Authorization":"OAuth "+api_key, 'Content-type':'application/x-www-form-urlencoded'}

# Convert the Nagios state to StatusPage state
def Nag2Status(state):
    if state == "CRITICAL":
        data = "component[status]=partial_outage"
    elif state == "WARNING":
        data = "component[status]=degraded_performance"
    elif state == "OK":
        data = "component[status]=operational"
    else:
        print(state)
        data = "Unknown"
    #print(data)
    return data

# Call the status page api and set the component status
addr = (url+page_id+"/components/"+comp_id+".json")
payload=Nag2Status(state)
response=requests.patch(addr, data=payload, headers=headers).content.decode()

# Some Debug if you please
#print(addr,headers,payload)
#print(response)