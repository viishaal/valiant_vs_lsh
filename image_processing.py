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

def resize_by_scale(image, scale):
	w,h = image.size
	w = int(w*scale)
	h = int(h*scale)
	return image.resize((w, h), Image.ANTIALIAS)

def resize_by_size(image, w, h):
	return image.resize((w, h), Image.ANTIALIAS)

def flatten_image_to_vector(image_arr):
	return image_arr.flatten()

def fetch_url(file_line):
	return file_line.split("\t")[1].split("\n")[0]

def is_flickr(url):
	return len(url.split("flickr.com")) > 1

def convert_img_to_vector(image, size_tuple, threshold):
	w,h = size_tuple
	img = resize_by_size(image, w, h)
	gray_img = convert_rgb_to_gray(img)
	binary_img = convert_gray_to_binary(gray_img, threshold)
	binary_arr = make_binary_array(binary_img)
	return flatten_image_to_vector(binary_arr)

def read_imageNet(index_range, pic_res):
	file = open("imageNet.txt")
	start,end = index_range
	urls = []
	matrix = []
	idx = 0
	while idx <= end:
		line = file.readline()
		url = fetch_url(line)
		if is_flickr(url):
			if idx >= start:
				urls.append(url)
				image = get_image_from_url(url)
				vec = convert_img_to_vector(image, pic_res, 100)
				matrix.append(vec)
			idx += 1
	matrix = np.array(matrix)
	file.close()
	return urls,matrix


