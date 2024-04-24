# Dog Breed Classifier

Welcome to the Dog Breed Classifier project! This application uses advanced machine learning techniques to identify the breed of dogs from images. Built with Python and leveraging PyTorch's powerful pre-trained models, this tool offers a fun and educational way to connect technology with our furry friends.

## Project Overview

The Dog Breed Classifier is designed to utilize convolutional neural networks provided by PyTorch's torchvision library to accurately predict dog breeds from provided images. It integrates various models, such as AlexNet, VGG, and ResNet, which have been trained on extensive datasets to ensure high accuracy and performance.

## Features

- **Breed Identification**: Determines the breed of dogs in images with high accuracy.
- **Support for Multiple Models**: Use different pre-trained neural network models for classification.

## Files and Directories

- `adjust_results4_isadog.py`: Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog'.
- `classifier.py`: Main script that handles the process of image classification.
- `print_results.py`: Outputs the results of the classification in a human-readable format.
- `pet_images/`: Directory containing sample images of pets.
- `uploaded_images/`: Directory where users can upload images for classification.
- `imagenet1000_clsid_to_human.txt`: Maps ImageNet IDs to human-readable labels.