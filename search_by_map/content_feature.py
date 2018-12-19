# python + opencv实现的内容特征算法 生成图片的指纹字符串 并存储到redis中的
# python content_feature.py -f n 计算图库中图片的指纹字符串
# python content_feature.py -p test_img/123.jpg 计算图片和图库中图片的相似度
import cv2 as cv
import os
from optparse import OptionParser
import numpy as np
import math
import hashlib
import redis
import itertools


def parse_options():
    parser = OptionParser(usage="")

    parser.add_option(
        '-p', '--path',
        dest="path",
        default="",
        help="输入图片路径"
    )
    parser.add_option(
        '-f', '--flag',
        dest="flag",
        default="y",
        help="y/n"
    )
    opts, args = parser.parse_args()
    return parser, opts, args

def content_feature(imgfile):
    """通过大津法找类间差异最大值的阈值进行二值化 w1*w2*(u1-u2)^2"""
    img=cv.imread(imgfile,  cv.IMREAD_GRAYSCALE) 
    img=cv.resize(img,(50,50),interpolation=cv.INTER_CUBIC)
    max_v = np.max(img)
    min_v = np.min(img)
    interclass_diffs = []
    h, w = img.shape[:2]
    for a in range(min_v, max_v+1):
        less_a = 0
        sum_less_a = 0
        sum_max_a = 0
        for r in range(h):
            for c in range(w):
                if img[r, c] <= a:
                    less_a += 1
                    sum_less_a += img[r, c]
                else:
                    sum_max_a += img[r, c]
        w1 = less_a/(h*w)
        w2 = 1-w1
        u1 = sum_less_a/less_a
        u2 = sum_max_a/(h*w - less_a) if sum_max_a != 0 else 0
        interclass_diff = w1*w2*(u1 - u2)**2
        interclass_diffs.append(interclass_diff)
    thres = min_v + interclass_diffs.index(max(interclass_diffs))
    
    img_list=list(itertools.chain.from_iterable(img.tolist()))
    avg_list = ['0' if i<=thres else '1' for i in img_list]

    return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,50*50,4)])

def cmpt(v1, v2):
    counter = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            if v1[i] != v2[i]:
                counter += 1
    else:
        counter = -1
    return (len(v1) - counter) * 1.0 / len(v1)

if __name__ == "__main__":
    pool = redis.ConnectionPool(max_connections=50, db=1)
    cnn = redis.StrictRedis(connection_pool=pool)
    parser, options, arguments = parse_options()
    path = options.path
    flag = options.flag
    images = os.listdir('tuku')
    if flag == 'n':
        for image in images:
            print(image)
            img_path = os.path.join('tuku', image)
            img_phash = content_feature(img_path)
            print(img_phash)
            key = ''.join(image.split('.'))
            if cnn.get(key):
                cnn.delete(key)
            cnn.append(key, img_phash)
    elif flag == 'y' and path:
        img_phash = content_feature(path)
        print(img_phash)
        for image in images:
            print(image)
            key = ''.join(image.split('.'))
            v = cnn.get(key).decode('utf-8')
            print(v)
            diff = cmpt(img_phash, v)
            print(diff)
    else:
        print('error')