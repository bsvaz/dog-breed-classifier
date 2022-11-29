# Use a Pre-trained Image Classifier to Identify Dog Breeds

## Installation

You can run this code on a environment with python3.9 and torchvision installed.
To install torchvision use:
`pip install torchvision`

## Project Motivation

This project is part of the "AI Programming with Python Nanodegree" program of Udacity.
The project uses CNN pre-trained image classifiers that was trained using ImageNet. The goal is to analyse the performance of different CNN Architectures classifying dog images.

## How to use this code

To run this code open a terminal in this folder and run the code:

`python check_images.py --dir <directory with images> --arch <model> --dogfile <file that contains dognames>`

To produce .txt files for each CNN Architectures like the "alexnet_pet-images.txt" run
`sh run_models_batch.sh`
for images on pet_images folder, or
`sh run_models_batch_uploaded.sh`

## Run your own images

To run your own images, upload them on the uploaded*images folder with names in the format "Dog_Breed*#.jpg", "Animal*Name*#.jpg" or "Object*Name*#.jpg", where "#" is a number, and run
`sh run_models_batch_uploaded.sh`
as above.
