import sys
import requests
import json

method = 'DELETE'
classifier_id = sys.argv[1]

url = 'https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers/' + str(classifier_id) + '?version=2018-03-19'
user = 'apikey'
password = '{key}'

print('url: ' + url)
response = requests.request(method, url, auth=(user,password))

print("http_code:" + str(response.status_code))
