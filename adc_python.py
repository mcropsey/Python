
"""
The general format for NITRO URLs is as follows:

For configurations. http://<netscaler-ip-address>/nitro/v1/config/<resource-type>

For retrieving statistics. http://<netscaler-ip-address>/nitro/v1/stat/<resource-type>



"""

import requests

with requests.Session() as s:
	p = s.get('http://192.168.1.31/nitro/v1/stat/appflow', auth=('admin', 'ZAQ!xsw2'))
	print(p.text)





