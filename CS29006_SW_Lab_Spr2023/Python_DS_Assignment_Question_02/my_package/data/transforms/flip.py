#Imports
from PIL import Image
import numpy as np

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        im1 = Image.open(image)
        hori_flip_im1 = im1.transpose(Image.FLIP_LEFT_RIGHT)
        im2 = hori_flip_im1
        return im2 , Image.fromarray(np.hstack((np.array(im1),np.array(im2))))


