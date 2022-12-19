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
    image_contoured = cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

    # fill contours --> cv2.drawContours(img, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)

    #print("Number of Contours is: " + str(len(contours)))

    '''
    rgb(0, 255, 0) Green
    rgb(127, 255, 0)
    rgb(255, 255, 0)
    rgb(255, 105, 0)
    rgb(255, 0, 0) Red
    '''

    rand = random.randint(1, 50)

    cv2.drawContours(image_contoured, contours, contourIdx = (2500 - rand), color=(255, 0, 0), thickness=cv2.FILLED)

    list_tables = []

    for i in range(50):
        tables = random.randint(1, 2450)
        list_tables.append(tables)
    
        cv2.drawContours(image_contoured, contours, contourIdx = tables, color=(0, 0, 255), thickness=cv2.FILLED)
    
    arr = np.asarray(list_tables)
    
    for i in range(2*len(arr)):
        if i%2 == 0: 
            pass
        else:
            arr = np.insert(arr, i, 5)
    
    arr = arr.reshape(int(len(arr)/2), 2)

    loop = 0
    
    # arr.T[0] = iteração pelo index das mesas
    # arr.T[1] = iteração pelo grau de satisfação das mesas
    
    while loop < 100:
        # Adicionar números aleatórios para as mesas
        array_of_tables_served = np.array(random.sample(list(arr.T[0]), 25))

        # Pintar cada cor com o grau de insatisfação do cliente
        for count, i in enumerate(arr.T[1]):
            if i == 5:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(44, 186, 0), thickness=cv2.FILLED)
            elif i == 4:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(163, 255, 0), thickness=cv2.FILLED)
            elif i == 3:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(255, 244, 0), thickness=cv2.FILLED)
            elif i == 2:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(255, 167, 0), thickness=cv2.FILLED)
            elif i == 1:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(255, 0, 0), thickness=cv2.FILLED)
            else:
                cv2.drawContours(image_contoured, contours, contourIdx = int(arr.T[0, count]), color=(0, 0, 0), thickness=cv2.FILLED)

        # Ver se o garçom passou pela mesa e diminuir a satisfação caso n tenha passado
        not_intersection = np.setxor1d(array_of_tables_served, arr.T[0])
        intersection = np.intersect1d(array_of_tables_served, arr.T[0])

        for common_table in not_intersection:
            for count, i in enumerate(arr.T[0]):
                if i == common_table and arr[count, 1] >= 1:
                    arr[count, 1] -= 1

        # Aumentar a satisfação em 1 caso passe
        for common_table in intersection:
            for count, i in enumerate(arr.T[0]):
                if i == common_table:
                    arr[count, 1] = 5

        x = frequency(arr.T[1])
        #print(x)
        #print("----------------------------------------------")
        plt.imshow(image_contoured)
        plt.show()
        
        loop += 1
        sample = []
        array_of_tables_served = []

def frequency(list): 
    freq = {}
    frequencias = np.array([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]])

    for item in np.unique(np.array(list)):
        freq[item] = np.where(np.array(list)==item)[0].shape[0]

    for key, value in freq.items(): 
        frequencias[key, 1] = value

    return frequencias
    
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