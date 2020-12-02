from skimage import data
import matplotlib.pyplot as plt
import numpy as np


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


# To threshold color images, convert themt o grayscale and then to threshold
image = data.text()

thresh = 127  # set temp threshold value
binary = image > thresh  # binary image = new thresh image

show_image(image, 'Original')
show_image(binary, 'Threshold Image')

# global or histogram based thresh : good for uniform background
# local or adaptive: best for uneven background illumination

from skimage.filters import try_all_threshold
plt.figure(1)
ax = try_all_threshold(image, verbose=False)
plt.show()

# Global Thresh
from skimage.filters import threshold_otsu
thresh = threshold_otsu(image)
binary_global = image > thresh

show_image(image, 'Original')
show_image(binary_global, 'Global Thresholding')

# Local Thresh
from skimage.filters import threshold_local

block_size = 35  #local neighborhood for the threshold
local_thresh = threshold_local(image, block_size, offset=10)
binary_local = image > local_thresh

show_image(image, 'Original')
show_image(binary, 'Local Threshold')
