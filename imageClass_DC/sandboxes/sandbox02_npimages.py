from skimage import color
from skimage import data
import matplotlib.pyplot as plt
import numpy as np


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


# red = image[:, :, 0]
# green = image[:, :, 1]
# blue = image[:, :, 2]

image = data.rocket()
vertically_flipped = np.flipud(image)
show_image(vertically_flipped, 'Vertically Flipped Image')

horizontally_flipped = np.fliplr(image)
show_image(horizontally_flipped, 'Horizontally Flipped Image')

red = image[:, :, 0]
plt.hist(red.ravel(), bins=256)
plt.title('Red Histogram')
plt.show()

blue = image[:, :, 2]
plt.hist(blue.ravel(), bins=256)
plt.title('Blue Histogram')
plt.show()

