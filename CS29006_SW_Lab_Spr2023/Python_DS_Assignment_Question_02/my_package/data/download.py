from PIL import Image
import requests
from io import BytesIO

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)

##d = Download()
#d.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\New folder (2)\sample.jpg", r"http://farm5.staticflickr.com/4127/5172389204_31214fdc50_z.jpg")
