def bg_color():
    return random.randint(200, 245)

def load_image(img):
    shadow = random.choice(['y', 'n'])
    shadow_l = random.randint(10, 15)
    print(shadow, shadow_l)
    fg, alpha = img[:, :, :3], img[:, :, 3]
    bg = np.ones(fg.shape, dtype=np.uint8) * bg_color()
    image = np.ones(fg.shape, dtype=np.uint8)
    rows, cols = fg.shape[:2]
    for r in range(rows):
        for c in range(cols):
            if alpha[r, c] == 0:
                b = random.randint(5, 10)
                f = random.choice(['+', '-'])
                if f == '+':
                    image[r, c, :] = bg[r, c, :] + b
                else:
                    image[r, c, :] = bg[r, c, :] - b
            else:
                image[r, c, :] = fg[r, c, :]
    if shadow == 'y':
        for r in range(rows):
            for c in range(cols):
                if alpha[r, c] and not alpha[r, c-1]:
                    for i in range(shadow_l):
                        if not alpha[r, c-1-i]:
                            image[r, c-1-i, :] = 10*i+70
                elif alpha[r, c] and not alpha[r, c+1]:
                    for i in range(shadow_l):
                        if not alpha[r, c+1+i]:
                            image[r, c+1+i, :] = 10*i+70
    return image


if __name__ == "__main__":
    import numpy as np

    import cv2 as cv
    import time
    import random
    random.seed(time.time())

    # ZAFUL = 'https://gloimg.zafcdn.com/'

    src_img = '1544554954800797563.png'

    img = cv.imread(src_img, cv.IMREAD_UNCHANGED)

    image = load_image(img)
    cv.imshow('src', image)
    cv.waitKey(0)
