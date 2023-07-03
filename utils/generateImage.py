from PIL import Image, ImageDraw, ImageFont

def generate_image(title):
    # Customize the image dimensions and text properties as per your requirements
    image_width = 400
    image_height = 200
    background_color = (255, 255, 255)  # White
    text_color = (0, 0, 0)  # Black
    font_size = 30

    # Load a fallback font
    font = ImageFont.truetype("fonts\night-pumpkind-font\NightPumpkind-1GpGv.ttf", font_size)

    # Create a blank image with the specified dimensions and background color
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Calculate the text position
    text_width, text_height = draw.textsize(title, font=font)
    text_x = (image_width - text_width) // 2
    text_y = (image_height - text_height) // 2

    # Draw the text on the image
    draw.text((text_x, text_y), title, font=font, fill=text_color)

    return image