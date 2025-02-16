#!/usr/local/bin/python
import requests
import json

print("\nSubdomain Enumeration Script\n")

def get_sub_domains(domain, filepath):
    url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains"
    querystring = {"children_only": "true"}
    headers = {
        'accept': "application/json",
        'apikey': "your_api_key"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result_json = json.loads(response.text)
    sub_domains = [i + '.' + domain for i in result_json['subdomains']]
    with open(filepath, 'w+') as f:
        for i in sub_domains:
            f.write(i + '\n')
    return sub_domains

domain = input("\nEnter Domain name: ")
filepath = input("\nPlease provide a file name to save: ")

get_sub_domains(domain, filepath)