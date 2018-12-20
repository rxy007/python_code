# 通过requests库请求url read图片 保存图片
# pil image convert mat 
# skimage read from url

import requests as req
from PIL import Image
import numpy as np
from io import BytesIO
import os
img_src = 'https://gloimg.zafcdn.com/zaful/pdm-product-pic/Clothing/2017/10/30/goods-first-img/1544554954800797563.png'
filename = img_src.split('/')[-1]
response = req.get(img_src)
with open(filename, 'wb') as f:
    f.write(response.content)
data = BytesIO(response.content)
print(type(data))
print(dir(data))
image = Image.open(data).convert('RGBA')
image = np.array(image)
print(image.dtype)
print(image.shape)
img_src = 'http://wx2.sinaimg.cn/mw690/ac38503ely1fesz8m0ov6j20qo140dix.jpg'
from skimage import io
image = io.imread(img_src)
print(image.dtype)
print(image.shape)