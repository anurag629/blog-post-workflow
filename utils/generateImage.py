from PIL import Image, ImageDraw, ImageFont
import os
import re

def generateImage(title, font_file, width=400, height=200):
    # Customize the image dimensions and text properties as per your requirements
    background_color = (255, 255, 255)  # White
    text_color = (0, 0, 0)  # Black
    font_size = 30

    # Load the specified font file
    font = ImageFont.truetype(font_file, 18)

    # Create a blank image with the specified dimensions and background color
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Calculate the text position
    text_width, text_height = draw.textsize(title, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw the text on the image
    draw.text((text_x, text_y), title, font=font, fill=text_color)

    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)
    title = re.sub(r'[^a-zA-Z\s]', '_', title)
    title = title.replace(' ', '_')
    image_path = os.path.join(images_dir, f"{title}.jpg")
    image.save(image_path)

    return f"/{image_path}"