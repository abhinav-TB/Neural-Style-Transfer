import argparse
from typing import Mapping
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from model import VGG
from train import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--style", help = "Style Image path" , required=True)
    parser.add_argument("-c", "--content", help = "Content Image path" , required=True)
    parser.add_argument("-e", "--epochs", help = "Number of Epocs" , required=True)
    parser.add_argument("-o", "--output", help = "Output Folder" , required=False)
    return parser.parse_args()



if __name__ == "__main__":
    

    args = parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    imsize = 356
    total_steps = int(args.epochs)
    learning_rate = 0.001
    alpha = 1
    beta = 0.01
    output_folder = "./output" if args.output is None else args.output

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


    train(original_img, style_img, generated, model, total_steps, alpha, beta, optimizer , output_folder)
