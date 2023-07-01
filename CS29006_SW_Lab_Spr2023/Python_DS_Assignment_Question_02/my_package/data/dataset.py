#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.data = []
        with jsonlines.open(annotation_file) as reader:
            self.count = 0
            for obj in reader:
                self.count+=1
                self.data.append(obj)
     

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return self.count 
    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.data[idx]

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        img = Image.open(path)
        return img
    
##a = Dataset(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\annotations.jsonl")
#a.__len__()
#data = a.__getann__(2)
#print(data['url'])

