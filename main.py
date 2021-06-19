import argparse
from typing import Mapping
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from model import VGG
from utils import *




if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--style", help = "Style Image path" , required=True)
    parser.add_argument("-c", "--content", help = "Content Image path" , required=True)
    parser.add_argument("-e", "--epochs", help = "Number of Epocs" , required=True)
    args = parser.parse_args()
 

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    imsize = 356
    total_steps = int(args.epochs)
    learning_rate = 0.001
    alpha = 1
    beta = 0.01

    loader = transforms.Compose(
        [
            transforms.Resize((imsize, imsize)),
            transforms.ToTensor(),
            # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    original_img = load_image(args.content , loader , device)
    style_img = load_image(args.style, loader , device)
    generated = original_img.clone().requires_grad_(True)
    model = VGG().to(device).eval()
    optimizer = optim.Adam([generated], lr=learning_rate)


    train(original_img, style_img, generated, model, total_steps, alpha, beta, optimizer)
