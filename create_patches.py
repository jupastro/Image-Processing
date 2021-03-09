#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:30:59 2021

@author: juliopastor

Function to create patches of a certain size in an image 
"""
import numpy as np

def create_patches( imgs,patch_size,add_noise=False,noise_level=0):
    ''' Create a list of  patches out of a list of images
    Args:
        imgs: list of input images
        patch_size:list including both dimensions (256,256)
        add_noise: boolean to add noise to the cropped image(useful for denoising previous steps or superresolution)
        noise_level: int between 0-255 representing the sd of the gaussian noise added
    ¡¡¡¡¡IMPORTANT if the image is not in a greyscale of 0-255 the noise must be rescaled in between 0-1 !!!!
        percentage_data:0-1 float specifying the percentage of data used for training
    Returns:
        list of image patches
    '''
    
    
    patches = [] #empty list to store the corresponding patches 
    patch_height=patch_size[0]
    patch_width=patch_size[1]
    for n in range( 0, len( imgs ) ):
        image = imgs[ n ]
        original_size = imgs[n].shape
        num_y_patches = original_size[ 0 ] // patch_size[0]#obtain the int number of patches that can be actually extracted from the original image
        num_x_patches = original_size[ 1 ] // patch_size[1]
        for i in range( 0, num_y_patches ):
            for j in range( 0, num_x_patches ):
              if add_noise:
                trainNoise = np.random.normal(loc=0, scale=noise_level, size=(patch_width,patch_height))
                patches.append(np.clip(image[ i * patch_width : (i+1) * patch_width,
                                      j * patch_height : (j+1) * patch_height ]+trainNoise,0,255)  )
              else:
                patches.append(image[ i * patch_width : (i+1) * patch_width,
                                      j * patch_height : (j+1) * patch_height ]  )
    
    return patches

"""EXAMPLE OF USE:
    # use method to create patches
train_img_patches = create_patches( train_img, patch_size=(256,256))
train_lbl_patches = create_patches( train_lbl, patch_size=(256,256))
#train_img_patches_noisy = create_patches( train_img,1,1,noise_level=20,add_noise=True)


# display one patch
# display first image
for i in range(0,8):
  plt.figure(figsize=(20,20))
  plt.subplot(8, 2, 1)
  plt.imshow( train_img_patches[i], 'gray' )
  plt.title( 'Input training patch' );
  # and its "ground truth"
  plt.subplot(8, 2, 2)
  plt.imshow( train_lbl_patches[i], 'gray' )
  plt.title( 'Ground truth patch' );

# We will use these patches as "ground truth" for training
"""
