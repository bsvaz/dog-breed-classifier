#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Bruno Vaz
# DATE CREATED: 11/28/2022
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print('Printing results...')
    print()
    print('Model architecture: ', model)
    print()
    print('Statistics results: ')
    stats_dic_names = {'n_images' : 'Number of images', 'n_dogs_img' : 'Number of dog images',
                        'n_notdogs_img' : 'Number of NON-dog images',
                        'n_match' : 'Number of matches between pet & classifier labels',
                        'n_correct_dogs' : 'Number of correctly classified dog images',
                        'n_correct_notdogs' : 'Number of correctly classified NON-dog images',
                        'n_correct_breed' : 'Number of correctly classified dog breeds',
                        'pct_match' : 'Percentage of correct matches',
                        'pct_correct_dogs' : 'Percentage of correctly classified dogs',
                        'pct_correct_breed' : 'Percentage of correctly classified dog breeds',
                        'pct_correct_notdogs' : 'Percentage of correctly classified NON-dogs'}\

    for key, value in results_stats_dic.items():
        print(' ', stats_dic_names[key], ': ', value)
    
    if print_incorrect_dogs == True:
        incorrect_dogs_keys = [key for key, value in results_dic.items() if 
                                value[3] != value[4]]
        print()
        print('Incorrect dog classified: ')
        for item in incorrect_dogs_keys:
            print(' ', item)

    if print_incorrect_breed == True:
        incorrect_breed_keys = [key for key, value in results_dic.items() if 
                                value[2] == 1 and value[3] == 1]
        print()
        print('Incorrect breed classified: ')
        for item in incorrect_breed_keys:
            print(' ', item)
