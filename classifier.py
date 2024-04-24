# REVISED DATE: 04/23/2024
# PROGRAMMER: Bruno Vaz

import ast
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

with open('./dog-breed-classifier/imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())


def classifier(img_path, model_version):

    img_pil = Image.open(img_path)

    # Get model and loading pre-trained weights
    if model_version in models.list_models():
        weights = models.get_model_weights(model_version)
        model = models.get_model(model_version, weights=weights)

    else:
        raise ValueError(f'{model_version} is not in the list of models from torchvision')

    # Preprocess image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    img_tensor = preprocess(img_pil).unsqueeze(0)
    
    # Set GPU if available
    if torch.cuda.is_available():
        model.cuda()
        img_tensor.cuda()
    
    else:
        print('GPU not available. Using CPU')
        
    # Inference
    model.eval()
    
    with torch.no_grad():
        output = model(img_tensor)
        
    pred_idx = output.squeeze().argmax().item()
    predict_class = imagenet_classes_dict[pred_idx]

    print(f'Predicted class: {predict_class}')
    return predict_class
