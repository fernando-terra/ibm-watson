from os import listdir
import base64
import sys

basepath = str('/home/ftsilva/fernandoterra/watson-dev/pictures/smart/')

#image1 = sys.argv[1]
count = 0

dirpos = str(basepath + 'training/positives/') 
dirneg = str(basepath + 'training/negatives/')

print(dirpos)
print(dirneg)

for img in listdir(dirpos):
#	print(img)
	with open(img, 'rb') as image_file:
		encoded_image = base64.b64encode(image_file.read())

	print(encoded_image)

#	for obj in listdir(dir):
#		image2 = str(dirneg + '/' + obj)
#		with open(image2, 'rb') as image_file:
#			encoded_analysis = base64.b64encode(image_file.read())
#
#		if(encoded_analysis == encoded_image):
#			count+=1
#
#	print(str(str(count) + ' arquivos como ' + image1 + ' existentes no repositorio'))
