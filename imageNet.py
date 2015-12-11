import requests
import requests_cache

requests_cache.install_cache()

AVAILABLE_SYNSET_URL = "http://www.image-net.org/api/text/imagenet.synset.obtain_synset_list"
SYNSET_NAME_PREFIX = "http://www.image-net.org/api/text/wordnet.synset.getwords?wnid="
IMAGE_URL_PREFIX = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid="

class ImageNet:
	def __init__(self, synset_indices):
		self.synset_indices = synset_indices
		self.all_wnids = self.get_synsets()
		self.wnid_list = []
		self.url_list = []
		for idx in self.synset_indices:
			self.url_list += self.get_synset_images(idx)

	def get_synsets(self):
		response = requests.get(AVAILABLE_SYNSET_URL)
		wnids = response.content.split("\n")
		return [x for x in wnids if x]

	def get_synset_name(self, wnid):
		url = ''.join([SYNSET_NAME_PREFIX, wnid])
		response = requests.get(url)
		return response.content

	def get_url_list(self, wnid):
		url = ''.join([IMAGE_URL_PREFIX, wnid])
		response = requests.get(url)
		urls = response.content.split("\r\n")
		return [x for x in urls if 'http:' in x]

	def get_synset_images(self, synset_index):
		synsets = self.get_synsets()
		self.wnid_list += synsets
		wnid = self.all_wnids[synset_index]
		print "getting synset: %s" % self.get_synset_name(wnid)
		return self.get_url_list(wnid)