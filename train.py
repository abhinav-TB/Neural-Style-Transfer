from PIL import Image
import torch
from torchvision.utils import save_image
def load_image(image_name , loader , device):
    image = Image.open(image_name)
    image = loader(image).unsqueeze(0)
    return image.to(device)

def train(original_img, style_img, generated, model, total_steps, alpha, beta, optimizer,output_folder ):
    for step in range(total_steps):
    # Obtain the convolution features in specifically chosen layers
        generated_features = model(generated)
        original_img_features = model(original_img)
        style_features = model(style_img)

    # Loss is 0 initially
        style_loss = original_loss = 0

    # iterate through all the features for the chosen layers
        for gen_feature, orig_feature, style_feature in zip(
        generated_features, original_img_features, style_features
    ):
        # batch_size will just be 1
            batch_size, channel, height, width = gen_feature.shape
            original_loss += torch.mean((gen_feature - orig_feature) ** 2)
        # Compute Gram Matrix of generated
            G = gen_feature.view(channel, height * width).mm(
            gen_feature.view(channel, height * width).t()
        )
        # Compute Gram Matrix of Style
            A = style_feature.view(channel, height * width).mm(
            style_feature.view(channel, height * width).t()
        )
            style_loss += torch.mean((G - A) ** 2)

        total_loss = alpha * original_loss + beta * style_loss
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
    print("total loss = " , total_loss.item())
    save_image(generated, f"{output_folder}/output.png")
    print("output saved")