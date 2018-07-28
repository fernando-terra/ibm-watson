import json
from watson_developer_cloud import VisualRecognitionV3

name_classifier='cars'

visual_recognition = VisualRecognitionV3 (
	version= '2018-03-19',
	iam_api_key = '{key}'
)

with open('/home/fernandoterra/watson-dev-cloud/carros.zip', 'rb') as positives, open(
	'/home/fernandoterra/watson-dev-cloud/nao_carros.zip', 'rb') as negatives:
	model = visual_recognition.create_classifier (
		name_classifier,
		cars_positive_examples=positives,
		negative_examples=negatives)

print(json.dumps(model, indent=2))
