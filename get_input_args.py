#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Bruno Vaz
# DATE CREATED: 11/10/2022                                 
# REVISED DATE: 

import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', action='store', dest='dir', default='pet_images/',
                        required=False, help='Image Folder')
    parser.add_argument('--arch', action='store', dest='arch', default='vgg',
                        required=False, help='CNN Model Architecture')
    parser.add_argument('--dogfile', action='store', dest='dogfile', default='dognames.txt',
                        required=False, help='Text File with Dog Names')    

    return parser.parse_args()
