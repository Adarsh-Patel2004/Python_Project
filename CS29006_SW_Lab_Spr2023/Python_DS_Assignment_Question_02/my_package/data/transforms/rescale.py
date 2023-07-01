#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.var = output_size
        if(type(output_size) is tuple):
            self.w, self.h = output_size

        else:
            self.x = output_size
            
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        im1 = Image.open(image)
        h , w = im1.size
        if(type(self.var) is tuple):
            im2 = im1.resize((round(self.w), round(self.h)))

        else:
            if(h<w):
                ratio = w/h
                new_width = int(ratio * self.x)
                im2 = im1.resize((self.x, new_width))
            else:
                ratio = h/w
                new_height = int(ratio * self.x)
                im2 = im1.resize((new_height, self.x))
        return im2



