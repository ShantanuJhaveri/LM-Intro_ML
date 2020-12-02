from skimage import color
from skimage import data
import matplotlib.pyplot as plt


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


# DISCOVERING SHAPE AND COLOR
coffee_image = data.coffee()
coins_image = data.coins()

print(coins_image.shape)
print(coffee_image.shape)

# convert rgb to grayscale
grayscaled_coffee = color.rgb2gray(coffee_image)
show_image(coffee_image, 'original')
show_image(grayscaled_coffee, 'grayscale image')