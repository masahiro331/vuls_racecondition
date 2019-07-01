import requests
import json

url = 'http://localhost:5515/vuls'

# openldap has 2 vulnerability. ['CVE-2014-8182', 'CVE-2015-6908']
data = {"Family": "amazon", "Release": "6.5-x86_64", "RunningKernel": {"Release": "2.6.32-431.23.3.el6.x86_64", "Version": ""}, "Packages": {"openldap-clients": {"Name": "openldap-clients", "Version": "2.4.23", "Release": "34.el6_5.1", "Arch": "x86_64"}}}

headers = {
    'Content-Type': 'application/json',
}

print("Loop requests... ")
while True:
    r_post_redhat = requests.post(url, headers=headers, json=data)
