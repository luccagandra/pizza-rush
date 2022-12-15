import cv2
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import math
import random

def main():
    path = '/home/lucca/Desktop/background.png'
    image = cv2.imread(path)   

    image_squared, lines, columns = draw_grid(image = image, grid_shape = [50,50], thickness = 2)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    image_contoured = cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    # fill contours --> cv2.drawContours(img, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)

    #print("Number of Contours is: " + str(len(contours)))

    rand = random.randint(1, 50)
    
    for i in range(len(contours)):
        if i > 50:
            break
        elif i == rand:
            cv2.drawContours(image_contoured, contours, contourIdx = (2500 - rand), color=(255, 0, 0), thickness=cv2.FILLED)

    plt.imshow(image_contoured)
    plt.show()

def draw_grid(image, grid_shape, color=(0, 0, 0), thickness=1):
    h, w, _ = image.shape
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols

    lines = []
    columns = []

    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv2.line(image, (x, 0), (x, h), color=color, thickness=thickness)
        lines.append(x)

    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv2.line(image, (0, y), (w, y), color=color, thickness=thickness)
        columns.append(y)

    return image, lines, columns

if __name__ == "__main__":
    main()