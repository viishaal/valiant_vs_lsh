import requests
from PIL import Image
import numpy as np
from StringIO import StringIO

def get_image_from_url(url):
	""" Fetch image file from url """
	response = requests.get(url)
	return Image.open(StringIO(response.content))

def get_image_array(image):
	return np.array(image);

def convert_rgb_to_gray(image):
	return image.convert('1');