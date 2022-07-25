import cv2
from matplotlib import pyplot
import os
from tqdm import tqdm
import numpy as np


def showimg(txtpath, imgpath):
    img = cv2.imread(imgpath)
    with open(txtpath) as f:
        s = f.readlines()
        for si in s:
            bbox_info = si.split()
            poly = np.array(bbox_info[:8], dtype=np.int32)
            pt1 = (poly[0], poly[1])
            pt2 = (poly[2], poly[3])
            pt3 = (poly[4], poly[5])
            pt4 = (poly[6], poly[7])
            cv2.circle(img, pt1, 4, (255, 255, 255))
            cv2.circle(img, pt2, 4, (255, 255, 255))
            cv2.circle(img, pt3, 4, (255, 255, 255))
            cv2.circle(img, pt4, 4, (255, 255, 255))
            cv2.imshow('image', img)
            cv2.waitKey(1000)
            print(poly)


if __name__ == '__main__':
    txtdir = './target/annfiles/'
    imgdir = './target/images/'
    txts = os.listdir(txtdir)
    for txt in tqdm(txts):
        imgname = txt[:-4] + '.png'
        showimg(txtdir + txt, imgdir + imgname)
