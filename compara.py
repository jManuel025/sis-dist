import numpy as np
import cv2

def compara(img1, img2):
    dif = cv2.subtract(img1, img2)
    if not np.any(dif):
        return True
    else: 
        return False