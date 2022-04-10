# This script defines some utility for the image resizes 

import cv2
import os


class ImageResizer():

    def __init__(self) -> None:
         pass

    def resize_image(self, path, filename, dest, width, height):
    
        img = cv2.imread(str.join(path, filename), cv2.IMREAD_UNCHANGED)
        print('Original Dimensions : ',img.shape)

        # new dimensions
        dim = (width, height)
  
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
        print('Resized Dimensions : ', resized.shape)
    
        cv2.imwrite(os.path.join(dest , filename), img)
        cv2.waitKey(0)


    def navigate_path(path):
        pass


    def setup():
        pass

if __name__ == "__main__":
    pass
