import requests
import json

url = 'http://localhost:5515/vuls'

data = {"Family": "ubuntu", "Release": "16.04_64", "RunningKernel": {"Release": "4.15.0-20-generic", "Version": ""}, "Packages": {"grub-gfxpayload-lists": {"Name": "grub-gfxpayload-lists", "Version": "0.7", "Release": "", "Arch": "amd64"}}}

headers = {
    'Content-Type': 'application/json',
}

for x in range(0,100):
    r_post = requests.post(url, headers=headers, json=data)
    res_json = json.loads(r_post.text)
