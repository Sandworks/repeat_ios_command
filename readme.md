# repeat_ios_command

**repeat_ios_command.py - gather information from multiple devices listed in a JSON file**

_James Sanders ' <ciscoguru72' *at* 'yahoo' *dot* 'com' *dot 'au'_

A python script to gather information from multiple devices that are listed in a JSON file. JSON file must have the following key:value pair - "name" for hostname and "ip" for ip address. The script allows you to perform a CLI command repetitively to multiple switches. The results are displayed on the screen. Other JSON key:value pair are ignored. Please see my "csv_json_convert" script to create a JSON file from CSV Spreadsheet.

I'm a network engineer who enjoys writing Python scripts to make life easy for myself and others. As a Python newbie, I'm always learning to improve my code. Therefore, I'm keen to hear your thoughts on my code and how I should improve. Also, I'm eager to hear new ideas and meet likewise people who write network-related Python scripts.
## Why?

I was asked to check the SNMP location on 22 switches, and I thought about this boring task and made this interesting by creating a python script to do this task for me. Going one step further, how about I create a script that allows me to run any CLI command across multiple switches.

## Userguide

**./repeat_ios_command.py _[JSON file] ["CLI Command"]_**

or 

**python3 repeat_ios_command.py _[JSON file] ["CLI Command"]_**

The script will read a JSON file and using its data to gather information based on the CLI command across multiple devices. For example:

**JSON file format**

JSON file must include these two key:value pair to make this script work, and they are "name" and "ip". Other key:value pairs are ignored. Here's an example JSON file:

![JSON Format](https://github.com/Sandworks/repeat_ios_command/blob/ed51f3c7ba45a51921b7277700b7664069b77621/json_format.png)

Using this json file, we can run the script as shown:

./repeat_ios_command.py device_list.json "show run | i snmp-server location

Here an example output from this script:

![SNMP Location](https://github.com/Sandworks/repeat_ios_command/blob/ed51f3c7ba45a51921b7277700b7664069b77621/snmp-location.png)

Another example using command "show ip int br | exclude unassigned"

![Mgmt-IP](https://github.com/Sandworks/repeat_ios_command/blob/ed51f3c7ba45a51921b7277700b7664069b77621/mgmt-ip.png)

## Additional Notes:

None.

Enjoy!

James.
