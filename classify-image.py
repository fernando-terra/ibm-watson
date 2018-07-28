import requests
import sys
import json

image = sys.argv[1]
classifier = sys.argv[2]

url = 'https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19'
user = 'apikey'
password = '{key}'

if(classifier=='default'):
	payload = {'classifier_ids':'default'}
elif(classifier=='cars'):
	payload = {'classifier_ids':'cars_317036151'}

images = {'images_file':open(image,'rb')}

response = requests.request("POST", url, files=images, data=payload, auth=(user, password))
data = json.loads(response.text)

print("http_code:" + str(response.status_code))
print(response.text)
