#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\annotations.jsonl")
    download = Download()

    #Print image names and their captions from annotation file using dataset object
    for i in range(10):
        data = dataset.__getann__(i)
        print(data['file_name'], data['captions'])
    print("\n")
    
    #Download images to ./data/imgs/ folder using download object
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\0.jpg", r"http://farm5.staticflickr.com/4127/5172389204_31214fdc50_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\1.jpg", r"http://farm8.staticflickr.com/7355/8825114508_b0fa4d7168_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg", r"http://farm8.staticflickr.com/7020/6478877255_242f741dd1_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\3.jpg", r"http://farm1.staticflickr.com/50/138352202_f4983aa717_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\4.jpg", r"http://farm4.staticflickr.com/3646/3426989867_e5b8439938_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\5.jpg", r"http://farm3.staticflickr.com/2253/1755223462_fabbeb8dc3_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\6.jpg", r"http://farm5.staticflickr.com/4088/4980393979_fb7325e0b6_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\7.jpg", r"http://farm4.staticflickr.com/3577/3491669985_d81e1050c6_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\8.jpg", r"http://farm3.staticflickr.com/2336/1634911562_703ff01cff_z.jpg")
    download.__call__(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\9.jpg", r"http://farm4.staticflickr.com/3446/3232237447_13d84bd0a1_z.jpg")

    #Transform the required image (roll number mod 10) and save it seperately
    flip = transforms[0]
    im1,im1_ = flip(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im1 = im1.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\flip.jpg")
    im1_ = im1_.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\flip_.jpg")
    blur = transforms[1]
    im2, im2_ = blur(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im2 = im2.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\blur.jpg")
    im2_ = im2_.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\blur_.jpg")

    rescale = RescaleImage((1280, 776))
    im3 = rescale(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im3 = im3.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rescale.jpg")
    rescale_ = RescaleImage((320, 194))
    im4 = rescale_(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im4 = im4.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rescale_.jpg")

    rotate = RotateImage(270)
    im5 = rotate(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im5 = im5.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rotate.jpg")
    rotate_ = RotateImage(45)
    im6 = rotate_(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg")
    im6 = im6.save(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rotate_.jpg")
    
    #Get the predictions from the captioner for the above saved transformed image
    model = ImageCaptioningModel()
    flip_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\flip.jpg", 3)
    blur_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\blur.jpg", 3)
    print("Captions for flipped image are: ")
    print(flip_caption)
    print("Captions for blurred image are: ")
    print(blur_caption)
    print("\n")

    print("Captions for 0.jpg image are: ")
    zero_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\0.jpg", 3)
    print(zero_caption)
    print("Captions for 1.jpg image are: ")
    one_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\1.jpg", 3)
    print(one_caption)
    print("Captions for 2.jpg image are: ")
    two_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\2.jpg", 3)
    print(two_caption)
    print("Captions for 3.jpg image are: ")
    three_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\3.jpg", 3)
    print(three_caption)
    print("Captions for 4.jpg image are: ")
    four_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\4.jpg", 3)
    print(four_caption)
    print("Captions for 5.jpg image are: ")
    five_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\5.jpg", 3)
    print(five_caption)
    print("Captions for 6.jpg image are: ")
    six_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\6.jpg", 3)
    print(six_caption)
    print("Captions for 7.jpg image are: ")
    seven_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\7.jpg", 3)
    print(seven_caption)
    print("Captions for 8.jpg image are: ")
    eight_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\8.jpg", 3)
    print(eight_caption)
    print("Captions for 9.jpg image are: ")
    nine_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\9.jpg", 3)
    print(nine_caption)
    print("\n")

    print("Captions for Twice Rescaled image (2X scaled) of 2.jpg image are: ")
    Re_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rescale.jpg", 3)
    print(Re_caption)
    print("Captions for Half Rescaled image (0.5X scaled) of 2.jpg image are: ")
    re_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rescale_.jpg", 3)
    print(re_caption)
    print("\n")

    print("Captions for 90 degree right rotated image of 2.jpg image are: ")
    Ro_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rotate.jpg", 3)
    print(Ro_caption)
    print("Captions for 45 degree left rotated image of 2.jpg image are: ")
    ro_caption = model(r"C:\Users\Welcome\OneDrive - iitkgp.ac.in\Desktop\Python Project\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\rotate_.jpg", 3)
    print(ro_caption)

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
