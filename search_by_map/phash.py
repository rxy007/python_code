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

def pHash(imgfile):
    """get image pHash value"""
    #加载并调整图片为32x32灰度图片
    img=cv.imread(imgfile,  cv.IMREAD_GRAYSCALE) 
    img=cv.resize(img,(64,64),interpolation=cv.INTER_CUBIC)

        #创建二维列表
    h, w = img.shape[:2]
    vis0 = np.zeros((h,w), np.float32)
    vis0[:h,:w] = img       #填充数据

    #二维Dct变换
    vis1 = cv.dct(cv.dct(vis0))
    #cv.SaveImage('a.jpg',cv.fromarray(vis0)) #保存图片
    vis1.resize(32,32)

    #把二维list变成一维list
    img_list=list(itertools.chain.from_iterable(vis1.tolist()))
    #计算均值
    avg = sum(img_list)*1./len(img_list)
    avg_list = ['0' if i<avg else '1' for i in img_list]

    #得到哈希值
    return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,32*32,4)])

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
    pool = redis.ConnectionPool(max_connections=50)
    cnn = redis.StrictRedis(connection_pool=pool)
    parser, options, arguments = parse_options()
    path = options.path
    flag = options.flag
    images = os.listdir('tuku')
    if flag == 'n':
        for image in images:
            print(image)
            img_path = os.path.join('tuku', image)
            # img_phash = main(img_path, 32)
            img_phash = pHash(img_path)
            print(img_phash)
            key = ''.join(image.split('.'))
            if cnn.get(key):
                cnn.delete(key)
            cnn.append(key, img_phash)
    elif flag == 'y' and path:
        # img_phash = main(path, 32)
        img_phash = pHash(path)
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
# 7ffffc0000000000fffffffff8000000fffffffffc000000fffffffff8000000fffffffffc000000fffffffff8000000fffffffffc000000fffffffff8000000fffffffffe000000fffffffff8000000fffffffffe000000ffffffffe8000000fffffffe7e000000fffffffe6e000000fffffffcbf000000fffffffffea00000