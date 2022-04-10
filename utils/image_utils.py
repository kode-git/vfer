# This script defines some utility for the image resizes 

import cv2
import os
import glob


class ImageWorker():

    def __init__(self) -> None:
         pass

    def format_converter(self, path, format_img, source_type, dest_path):
        """format_converter str

        Args:
            path (str): The source path of the images folder 
            format (str): Format of the images in the folder
            source_type (str): Type of the dataset 
            dest_path (str): Destination path to store resized images
        """        
        count = 0
        os.mkdir(dest_path)
        for file in glob.glob(path + "/*." + format_img):
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            resized = cv2.resize(img, (224,224), interpolation=cv2.INTER_CUBIC)
            print('Resized writing for', dest_path + "resized_on_" + source_type + "_" + str(count) + "." + format_img )
            cv2.imwrite(dest_path + "resized_on_" + source_type + "_" + str(count) + "."+ format_img, resized)
            count += 1

    def navigate_path(self, path):
        """navigate_path

        Args:
            path (str): Path to navigate and counting number of files

        Returns:
            int : the total amount of file in the directory specified by the path
        """        
        count = 0
        for dir in os.listdir(path):
            if os.path.isfile(os.path.join(path, dir)):
                count += 1
        print('Counter for', path, ':', count)
        return count


    def setup():
        pass

if __name__ == "__main__":
    iw = ImageWorker()
    origin_path = input("Tell the origin path: ")
    dest_path = input("Tell the destination path: ")
    format = input("Tell the images format: ")
    source_type = input('Tell me the format: ')
    iw.format_converter(origin_path, format, source_type, dest_path)


