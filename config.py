
# -*- coding: utf-8 -*-
import os

cur_path = os.path.dirname(os.path.abspath(__file__))

CLASSES = ["1"]  # the name of the classes ,pay attention to the index of the class

# train data and validate data
TRAIN_TXT_PATH = os.path.join(cur_path, 'data', 'train.txt')
VAL_TXT_PATH = os.path.join(cur_path, 'data', 'val.txt')

# origin data
IMAGE_FOLDER = os.path.join(cur_path, 'imgs')  # origin img folder
LABEL_FOLDER = os.path.join(cur_path, 'label')  # origin lable folder ,it contain's the xml label result
