# This script defines some utility for the image resizes 

import cv2
import os
import glob


class ImageWorker():

    def __init__(self) -> None:
         pass

    def format_converter(self, path, format, dest_path):
        count = 0
        os.mkdir(dest_path)
        for file in glob.glob(path + "/*." + format):
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            resized = cv2.resize(img, (224,224), interpolation=cv2.INTER_CUBIC)
            print('Resized writing for', dest_path + "resized_" + str(count) + "." + format )
            cv2.imwrite(dest_path + "resized_" + str(count) + "." + format, resized)
            count += 1

    def navigate_path(self, path):
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
    iw.format_converter(origin_path, format, dest_path)


