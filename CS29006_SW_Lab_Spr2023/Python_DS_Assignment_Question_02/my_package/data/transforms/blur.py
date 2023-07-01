#Imports
from PIL import Image, ImageFilter
import numpy as np

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''
    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)'''
        im1 = Image.open(image)
        im2 = im1.filter(ImageFilter.GaussianBlur(self.radius))
        return im2 , Image.fromarray(np.hstack((np.array(im1),np.array(im2))))
