#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Bruno Vaz
# DATE CREATED: 11/10/2022                         
# REVISED DATE: 

# Imports python modules
from os import listdir
import re

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    results_dic = {}

    for filename in listdir(image_dir):
        if filename[0] != '.':
            label = re.sub(r'[0-9]', '', filename)
            label = re.sub('.jpg', '', label)
            label = re.sub('_', ' ', label)
            label = label.strip()
            label = label.lower()

            results_dic[filename] = [label]

    return results_dic


