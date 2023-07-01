#Imports
from PIL import Image
import PIL

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self.degrees = degrees
        
    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        im1 = Image.open(sample)
        im1 = im1.rotate(self.degrees, PIL.Image.NEAREST, expand = 1)
        return im1
