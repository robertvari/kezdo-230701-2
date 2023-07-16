from PIL import Image, ImageDraw, ImageFont
import os
from my_functions.get_all_files import get_all_files


def main(root_folder, text="Watermark", font_size=40):
    # collect all files
    files = []
    get_all_files(root_folder, files)

    # get all image files
    image_files = collect_image_files(files)

    for image_file in image_files:
        process_image(image_file)

def collect_image_files(file_list) -> list:
    image_files = []

    allowed_extensions = [".jpg", ".jpeg"]
    for file in file_list:
        extension = os.path.splitext(file)[-1]
        if not extension.lower() in allowed_extensions:
            continue

        image_files.append(file)

    return image_files

def process_image(image_file, text, font_size):
    img = Image.open(image_file)

    # resize image
    img.thumbnail((1000, 1000))
    img_width = img.size[0]
    img_height = img.size[1]

    # create an empty canvas layer
    text_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))

    # create draw context
    draw = ImageDraw.Draw(text_layer)

    # create font
    font = ImageFont.truetype("watermark.ttf", font_size)
    text_box = font.getbbox(text)
    text_width = text_box[2]
    text_height = text_box[3]

    margin = 20

    # write text
    x = img_width - text_width - margin
    y = img_height - text_height - margin
    draw.text((x,y), text, fill=(255, 255, 255, 100), font=font)
    
    # merge text_layer and image
    img = Image.alpha_composite(img, text_layer).convert("RGB")

    save_image(img, image_file)

def save_image(image, image_file):
    pass


main(
    root_folder=r"D:\Work\_PythonSuli\kezdo-230701\photos", 
    text="Robert Vari Photography"
)