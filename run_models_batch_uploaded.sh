#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch_uploaded.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: 02/27/2018  - 
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh    -- will run program from commandline within Project Workspace
#  
python ./dog-breed-classifier-2/check_images.py --dir ./dog-breed-classifier-2/uploaded_images/ --arch resnet50  --dogfile ./dog-breed-classifier-2/dognames.txt > ./dog-breed-classifier-2/resnet50_uploaded-images.txt
python ./dog-breed-classifier-2/check_images.py --dir ./dog-breed-classifier-2/uploaded_images/ --arch alexnet --dogfile ./dog-breed-classifier-2/dognames.txt > ./dog-breed-classifier-2/alexnet_uploaded-images.txt
python ./dog-breed-classifier-2/check_images.py --dir ./dog-breed-classifier-2/uploaded_images/ --arch vgg19  --dogfile ./dog-breed-classifier-2/dognames.txt > ./dog-breed-classifier-2/vgg19_uploaded-images.txt
