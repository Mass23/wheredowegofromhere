import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import glob
import random
import cv2
import os
from skimage.util import random_noise
import subprocess

def ProcessFrame(frame):
    frame = np.asarray(frame)
    frame = random_noise(frame, mode='gaussian', var=0.4)
    frame_final = (255*frame).astype(np.uint8)
    return(frame_final)


plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 19

def ProcessPhotos():
    np.random.seed(10000)

    ############################################################################
    # Palestine
    img = plt.imread('GAZA.png')

    for size in [50000, 40000, 30000, 25000, 20000, 15000, 10000, 7500, 5000, 2500, 2000, 1500, 1000, 500, 250]:
        plt.scatter(0,750,zorder=1,c='#EE2A35',s=size, alpha=0.1) # Red
        plt.scatter(1250,0,zorder=1,c='#000000',s=size, alpha=0.1) # Black
        plt.scatter(1250,1500,zorder=1,c='#009736',s=size, alpha=0.1) # Green
        plt.scatter(750,750,zorder=1,c='#FFFFFF',s=size, alpha=0.1) # White

    plt.imshow(img, zorder=0, extent=[0, 1500, 0, 1500])
    plt.axis('off')
    plt.savefig('WDWGFH_scatter.png', bbox_inches = 'tight', pad_inches = 0, dpi=1000)
    plt.close()

    img = cv2.imread('WDWGFH_scatter.png')
    img = ProcessFrame(img)
    cv2.imwrite('WDWGFH_noise.png', img)

    img = plt.imread('WDWGFH_noise.png')
    plt.imshow(img, zorder=0, extent=[0, 1500, 0, 1500])
    plt.text(50, 725, 'Where do we go from here?', style='italic', weight='bold', c='#00000C')
    plt.axis('off')
    plt.savefig('WDWGFH_text.png', bbox_inches = 'tight', pad_inches = 0, dpi=1000, facecolor='#448E5E')
    plt.close()

def Main():
    ProcessPhotos()
    # example to generate glitches: glitch_this -o out_file.png in_file.png [0-10]
Main()
