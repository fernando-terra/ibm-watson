import requests
import sys
import json

#classifier = sys.argv[1]
classifier = 'cars'

url = 'https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers/' + str(classifier) + '?version=2018-03-19'
user = 'apikey'
password = '{key}'

payload = {}
header = {}

response = requests.request("GET",url, auth=(user, password))

if(response.status_code == requests.codes.ok):
	data = json.loads(response.text)
	print("http_code:" + str(response.status_code) + " | network_status: " + data['status'] + " | classifier_id: " + data['classifier_id'])
else:
	print("http_code:" + str(response.status_code))
