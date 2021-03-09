# Image-Processing
Functions to process images in order to make them suitable for Deep Learning tasks

* **create_patches.py**- is a function that allows you to obtain a certain amount of cropped patches from the original image with the desired size. Useful when you're dealing with different size images or in order to obtain more training images. It can also add Gaussian noise to the images if desired to be used in a pretraining step or for Denoising purposes. 

* **add_Gaussian_Noise**- is a function that allows you to add Normal Gaussian Noise N(0,std) to images by selecting a certain percentage of noise that will be used as the std of the Gaussian distribution.
