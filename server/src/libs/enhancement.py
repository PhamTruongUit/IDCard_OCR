import numpy as np

def contract_brightness (image, contract=1.5, brightness=-70):
    temp = np.array(image)
    image = np.zeros_like(temp)
    image = (temp-0.5)*contract + 0.5 + brightness
    image = np.rint(image)
    image[image > 255] = 255
    image[image < 0] = 0
    return image.astype(np.uint8)