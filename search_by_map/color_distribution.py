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

def color_distribution(imgfile):
    """get image pHash value"""
    img=cv.imread(imgfile,  cv.IMREAD_UNCHANGED)
    color_list = [0]*64
    rows, cols = img.shape[:2]
    for r in range(rows):
        for c in range(cols):
            # print(''.join(map(str, (img[r, c, :]//64).tolist())))
            p = ''.join(map(str, (img[r, c, :3]//64).tolist()))
            i = int(p, 4)
            color_list[i] += 1
    return ','.join(map(str, color_list))
    # return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,50*50,4)])

def cosine_similarity(v1, v2):
    v1_arr = np.array(list(map(int, v1.split(',')))).astype(np.float)
    v2_arr = np.array(list(map(int, v2.split(',')))).astype(np.float)
    # print(v1_arr.dtype)
    num = np.dot(v1_arr, v2_arr)
    denom = np.linalg.norm(v1_arr) * np.linalg.norm(v2_arr)
    cos = num / denom
    print(cos)
    return cos


def pearson(v1, v2):
    v1_arr = np.array(list(map(int, v1.split(',')))).astype(np.float)
    v2_arr = np.array(list(map(int, v2.split(',')))).astype(np.float)
    v1_mean = np.mean(v1_arr)
    v2_mean = np.mean(v2_arr)
    v1_arr = v1_arr - v1_mean
    v2_arr = v2_arr - v2_mean
    num = np.dot(v1_arr, v2_arr)
    denom = np.linalg.norm(v1_arr) * np.linalg.norm(v2_arr)
    pearson = num/denom
    print(pearson)
    return pearson

if __name__ == "__main__":
    pool = redis.ConnectionPool(max_connections=50, db=2)
    cnn = redis.StrictRedis(connection_pool=pool)
    parser, options, arguments = parse_options()
    path = options.path
    flag = options.flag
    images = os.listdir('tuku')
    if flag == 'n':
        for image in images:
            print(image)
            img_path = os.path.join('tuku', image)
            img_phash = color_distribution(img_path)
            print(img_phash)
            key = ''.join(image.split('.'))
            if cnn.get(key):
                cnn.delete(key)
            cnn.append(key, img_phash)
    elif flag == 'y' and path:
        img_phash = color_distribution(path)
        print(img_phash)
        for image in images:
            print(image)
            key = ''.join(image.split('.'))
            v = cnn.get(key).decode('utf-8')
            print(v)
            diff = cosine_similarity(img_phash, v)
            diff = pearson(img_phash, v)
    else:
        print('error')