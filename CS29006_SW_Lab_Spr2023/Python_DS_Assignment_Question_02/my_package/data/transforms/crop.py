#Imports
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.h, self.w = shape
        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        im1 = Image.open(image)
        width, height = im1.size
        left = (width - self.w)/2
        top = (height - self.h)/2
        right = (width + self.w)/2
        bottom = (height + self.h)/2
        im2 = im1.crop((left, top, right, bottom))
        return im2

