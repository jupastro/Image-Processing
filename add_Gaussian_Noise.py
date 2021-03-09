#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:56:03 2021

@author: juliopastor
Function to add Gaussian noise of N(0,std) to an image
"""


import numpy as np
import matplotlib.pyplot as plt
def add_Gaussian_Noise(image,percentage_of_noise,print_img=False):
  """
  image: greyscale image to be added Gaussian Noise with 0 mean and a certain std
  percentage_of_noise:similar to 1/SNR, it represents the % of 
  the maximum value of the image that will be used as the std of the Gaussian Noise distribution
  """
  max_value=np.max(image)
  noise_level=percentage_of_noise*max_value
  Noise = np.random.normal(loc=0, scale=noise_level, size=image.shape)
  noisy_img=np.clip(image+Noise,0,max_value)  
  if print_img:
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow( image, 'gray' )
    plt.title( 'Original image' );
    # and its "ground truth"
    plt.subplot(1, 2, 2)
    plt.imshow( noisy_img, 'gray' )
    plt.title( 'Noisy image' );
  
  return noisy_img

