from image_processing import *

url1 = "http://breadedcat.com/wp-content/uploads/2012/02/cat-breading-tutorial-004.jpg"
url2 = "http://images.natureworldnews.com/data/images/full/15186/worried-cat.jpg"
image = get_image_from_url(url1)
gray_img = convert_rgb_to_gray(image)
binary_img = convert_gray_to_binary(gray_img, 125)
if (binary_img!=None): binary_img.show()
print "binary image matrix:"
print make_binary_array(binary_img)