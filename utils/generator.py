from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy import expand_dims
from matplotlib import pyplot


def generator(path, format_img, dest_path,source_type):
        gen= ImageDataGenerator(
            featurewise_center=True,
            featurewise_std_normalization=True,
            rotation_range=10,
            width_shift_range=0.2,
            height_shift_range=0.2,
            brightness_range=(0.2,0.8),
            zoom_range=0.2,
            horizontal_flip=True
            #preprocessing_function=
            )
        print("This is:", navigate_path(dest_path))
        if navigate_path(dest_path) == 0:
            os.mkdir(dest_path)
        for file in glob.glob(path + "\\*." + format_img):
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            print(img.shape)
         
            # convert to numpy array
            # expand dimension to one sample
            samples = expand_dims(img, 0)
            iterator = gen.flow(samples,batch_size=1)
            for i in range(9):
                pyplot.subplot(330 + 1 + i)
                batch = iterator.next()
                image = batch[0].astype('uint8')
                pyplot.imshow(image)
            pyplot.show()
            cv2.imwrite(dest_path + "augmented_on_" + source_type + "_" + str(1) + "."+ format_img, aug_image)


def navigate_path(path):
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
        return count
generator('C:\\Users\\bigfo\\OneDrive\\Documents\\GitHub\\visual-transformers-emotion-recognition\\utils',"png","C:\\Users\\bigfo\\OneDrive\\Documents\\GitHub\\visual-transformers-emotion-recognition\\utils","png")
