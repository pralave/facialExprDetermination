import cv2, os
import numpy as np
from PIL import Image

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.face.createLBPHFaceRecognizer()#sthash.B60n4b7E.dpuf

def get_images_and_labels(path):
	image_paths = [os.path.join(path,f) for f in os.listdir(path) if not f.endswith(".sad")]
	images = []
	labels = []

	for image_path in image_paths:
		image_pil = Image.open(image_path).convert('L')
		image = np.array(image_pil, 'uint8')
		# cv2.imshow('image', image)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
		nbr = int(os.path.split(image_path)[1].split('.')[0].replace('subject',""))
		faces = faceCascade.detectMultiScale(image)

		for (x,y,w,h) in faces:
			images.append(image[y: y+h, x: x+w])
			labels.append(nbr)
			cv2.imshow("Adding faces to training set...", image[y: y+h, x: x+w])
			cv2.waitKey(50)

	return images, labels

path = "yalefaces"
images. labels = get_images_and_labels(path)
cv2.destroyAllWindows()