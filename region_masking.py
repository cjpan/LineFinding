import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('d:\\test.jpg')
print('This image is: ', type(image), 'with dimensions: ', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

# copy the image instead simply using:
color_select = np.copy(image)

red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

thresholds = (image[:, :, 0] < rgb_threshold[0]) \
             | (image[:, :, 1] < rgb_threshold[1]) \
             | (image[:, :, 2] < rgb_threshold[2])
color_select[thresholds] = [0, 0, 0]

# print(thresholds)
# print(color_select)

plt.imshow(color_select)
plt.show()

mpimg.imsave("d:\\test-after.jpg", color_select)
