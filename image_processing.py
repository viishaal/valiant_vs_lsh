import requests
from PIL import Image
import numpy as np
from StringIO import StringIO

def get_image_from_url(url):
	""" Fetch image file from url """
	response = requests.get(url)
	return Image.open(StringIO(response.content))

def get_image_array(image):
	return np.array(image, dtype="int");

def convert_rgb_to_gray(image):
	return image.convert('L');

def convert_gray_to_binary(image, threshold):
	if image.mode == "L":
		binary = image.point(lambda p: p > threshold and 255)
		return binary
	else:
		print "invalid image!"
		return None

def make_binary_array(image):
	arr = get_image_array(image)
	for r in xrange(arr.shape[0]):
		for c in xrange(arr.shape[1]):
			if arr[r,c] == 0:
				arr[r,c] = -1
			else:
				arr[r,c] = 1
	return arr