# -*- coding: utf-8 -*-
import os

import xml.etree.ElementTree as ET

import config as cf


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]

    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return (x, y, w, h)


def convert_annotation(image: str):
    """
    :param image: image path
    get the xml label input file ,generate the image box txt file
    """
    xml_file = os.path.join(cf.LABEL_FOLDER, image.replace('.jpg', '.xml'))
    txt_file = os.path.join(cf.IMAGE_FOLDER, image.replace('.jpg', '.txt'))

    in_file = open(xml_file)
    out_file = open(txt_file, 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)  #

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in cf.CLASSES:
            continue

        cls_id = cf.CLASSES.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text),
             float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    # release the file stream
    in_file.close()
    out_file.close()


def gen_train_data():
    train_file = open(cf.TRAIN_TXT_PATH, 'w')

    for img in os.listdir(cf.IMAGE_FOLDER):
        if 'jpg' not in img:
            continue

        # 这里改为样本图片所在文件夹的路径
        train_file.write(os.path.join(cf.IMAGE_FOLDER, img) + '\n')
        convert_annotation(img)

    train_file.close()
    print('finish!')


def split_validate_path():
    pass


if __name__ == '__main__':
    gen_train_data()
