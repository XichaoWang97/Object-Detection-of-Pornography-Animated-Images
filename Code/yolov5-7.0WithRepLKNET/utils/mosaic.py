import cv2
import numpy as np

# 常规马赛克
def conventional_mosaic(img, x, y, w, h, neighbor=9):
    """
    :param rgb_img
    :param int x :  马赛克左顶点
    :param int y:  马赛克左顶点
    :param int w:  马赛克宽
    :param int h:  马赛克高
    :param int neighbor:  马赛克每一块的宽
    """
    for i in range(0, h, neighbor):
        for j in range(0, w, neighbor):
            rect = [j + x, i + y]
            color = img[i + y][j + x].tolist()  # 关键点1 tolist
            left_up = (rect[0], rect[1])
            x2 = rect[0] + neighbor - 1  # 关键点2 减去一个像素
            y2 = rect[1] + neighbor - 1
            if x2 > x + w:
                x2 = x + w
            if y2 > y + h:
                y2 = y + h
            right_down = (x2, y2)
            cv2.rectangle(img, left_up, right_down, color, -1)  # 替换为为一个颜值值
    return img

# 高斯马赛克
def gaussian_mosaic(img, x1, y1, x2, y2):
    img[y1:y2, x1:x2, 0] = np.random.normal(size=(y2 - y1, x2 - x1))
    img[y1:y2, x1:x2, 1] = np.random.normal(size=(y2 - y1, x2 - x1))
    img[y1:y2, x1:x2, 2] = np.random.normal(size=(y2 - y1, x2 - x1))
    return img