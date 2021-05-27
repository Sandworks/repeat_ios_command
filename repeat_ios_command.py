#!/usr/bin/env python3

# Filename: repeat_ios_command.py
# Author:   James Sanders
# Version:  1.0

# Import dependencies
import json
import sys
from netmiko import ConnectHandler
from getpass import getpass
from pythonping import ping

# Obtain device credentials
def credentails():
    username = input('Username: ')
    password = getpass(prompt='password: ')
    return username, password

# Get result from CLI command
def cli(net_connect, command):
    return net_connect.send_command(command)

# Connect and run CLI command entered
def connect_run_command():
    for device in devices['devices']:
        try:
            # Try SSH
            connect_device = {
                'device_type': 'cisco_ios_ssh',
                'ip': device['ip'],
                'username': username,
                'password': password
            }
            service = 'ssh'
            net = ConnectHandler(**connect_device)
            print("\n{} ({}):".format(device['name'], device['ip']))
            print(cli(net, command))
        except:
            # If ssh failed, try telnet
            try:
                connect_device = {
                    'device_type': 'cisco_ios_telnet',
                    'ip': device['ip'],
                    'username': username,
                    'password': password,
                    'secret': password,
                    'port': 23,
                }
                service = 'telnet'
                net = ConnectHandler(**connect_device)
                print("\n{} ({}):".format(device['name'], device['ip']))
                print(cli(net, command))
            except:
                #this is the catch all except, if NOTHING works, tell the user and continue onto the next item in the for loop.
                print("{} ({}): Unable to connect!".format(device['name'], device['ip']))
                continue

# check we received correct argument.
if len(sys.argv) == 3:
    jsonfile = sys.argv[1]
    command = sys.argv[2]

elif len(sys.argv) == 1:
	sys.exit("Usage: {} <json file> <command>".format(sys.argv[0]))	

elif len(sys.argv) > 3:
	print ("Too many arguments")
	sys.exit()

# credentails
username, password = credentails()

# gather device details from a JSON file
with open(jsonfile) as file:
    devices = json.load(file)

# Loop each device, and for each device get result from CLI command entered
connect_run_command()

# task complete    
print ('\nTask complete')
