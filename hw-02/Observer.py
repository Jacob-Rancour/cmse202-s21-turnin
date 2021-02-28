from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename) 
        
    def load_images(self,im1_filename,im2_filename):
        image_data_red = fits.getdata(self.im1_filename)
        image_data_ir = fits.getdata(self.im2_filename)
        image = {}
        image[self.im1_filename] = image_data_red
        image[self.im2_filename] = image_data_ir
        return image
    
    def make_composite(self,im_dict):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        ir_hud_list = fits.open(self.im2_filename)[0]
        wcs = WCS(ir_hud_list.header)
        # Define the array for storing RGB values
        rgb = np.zeros((im_dict[self.im1_filename].shape[0],im_dict[self.im1_filename].shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = im_dict[self.im1_filename].astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (im_dict[self.im2_filename].astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
            # Define the array for storing RGB values
        rgb = np.zeros((im_dict[self.im1_filename].shape[0],im_dict[self.im1_filename].shape[1],3))
    
    # Define a normalization factor for our denominator using the R filter image
        norm_factor = im_dict[self.im1_filename].astype("float").max()
    
    # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = (im_dict[self.im2_filename].astype("float")/norm_factor) * 1.5
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
    
        rgb[:,:,1] = ((im_dict[self.im2_filename].astype("float")+ im_dict[self.im1_filename].astype("float"))/2)/norm_factor
    
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
    
        rgb[:,:,2] = (im_dict[self.im2_filename].astype("float"))/norm_factor
    
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0
        
        plt.subplot(projection = wcs)
        plt.xlabel('Right Acension')
        plt.ylabel('Declination')
        plt.grid(color='white')
        plt.imshow(rgb)

    def calc_stats(self):
        listm = []
        lists = []
        for i in 
        return mean, std
