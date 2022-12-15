import cv2
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    path = '/home/lucca/Desktop/background.png'
    image = cv2.imread(path)   

    image_squared, lines, columns = draw_grid(image = image, grid_shape = [50,50], thickness = 2)

    plt.imshow(image_squared)
    plt.show()

def draw_grid(image, grid_shape, color=(255, 255, 255), thickness=1):
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