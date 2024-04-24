#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#                                                                            
# PROGRAMMER: Bruno Vaz
# DATE CREATED: 11/04/2022                               
# REVISED DATE: 
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Import torch
import torch

# Main program function defined below
def main():
    
    # Measures total program runtime by collecting start time
    start_time = time()
    
    # Get inputs from command line
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

    # Create pet labels
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the Results Dictionary using results    
    check_creating_pet_image_labels(results)

    print() # Only to jump a line.

    # Set device
    if torch.cuda.is_available():
        device = 'cuda'
        print('GPU is available. Used GPU.')
    else:
        device = 'cpu'
        print('GPU is not available. Used CPU.')

    # Function that classify the images and update Results Dictionary with those
    classify_images(in_arg.dir, results, in_arg.arch, device)

    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images 'as a dog' or 'not a dog' 
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using 
    # results
    check_classifying_labels_as_dogs(results)

    # Calculates statistics of the results
    results_stats = calculates_results_stats(results)

    print() # Only to jump a line

    # Print the results
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()
    
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time  #calculate difference between end time
                                      #and start time
    print("\n** Total Elapsed Runtime: {}:{}:{}".format(
          str(int((tot_time/3600))), str(int((tot_time%3600)/60)), 
          str(int((tot_time%3600)%60)) ))
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
