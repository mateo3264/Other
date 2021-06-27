import numpy as np
import cv2
from PIL import Image
from escaneo_array2x2 import get_new_state_of_cell

import os


rows = cols = 128


den = 4
z = np.zeros((rows,cols),dtype=np.int8)

y_idxs,x_idxs = np.random.randint((rows//2)-rows//den,(rows//2)+rows//den,size=rows*4),np.random.randint((cols//2)-cols//den,(cols//2)+cols//den,size=cols*4)

z[y_idxs,x_idxs] = 255

z_pad = np.pad(z,(1,1),constant_values=(-2,-2))

n_timesteps = 10000


for i in range(n_timesteps):
    z = z_pad.copy()
    for r in range(rows):
        for c in range(cols):
            orig_w = z_pad[r:r+3,c:c+3]
            w = orig_w.copy()
            living = w[1,1]
            
            w[1,1] = get_new_state_of_cell(orig_w,living)
            t = np.all(w==orig_w)
            z[r + 1,c + 1] = w[1,1]
    img = Image.fromarray(z[1:rows+1,1:cols+1],'L')
    img = img.resize((256,256),Image.NEAREST)
    


    cv2.imshow('Game of Life',np.array(img))
    cv2.waitKey(1)
    
    z_pad = z.copy()
