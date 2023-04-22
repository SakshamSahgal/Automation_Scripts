import os
import sys
import argparse
from PIL import Image
import pyheif

def convert_images(input_dir, output_dir):
    # Make output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in input directory
    for file_name in os.listdir(input_dir):
        # Skip if file is not a HEIC file
        if not file_name.lower().endswith(('.heic', '.HEIC')):
            continue

        # Open image file
        image_file = os.path.join(input_dir, file_name)
        with open(image_file, 'rb') as f:
            image = Image.frombytes(data=pyheif.read(f).data, mode=pyheif.read(f).mode, size=pyheif.read(f).size)

        # Save image in PNG format
        new_file_name = os.path.splitext(file_name)[0] + '.png'
        new_file_path = os.path.join(output_dir, new_file_name)
        image.save(new_file_path, 'PNG')

        print(f"Converted {file_name} to {new_file_name}")

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Batch convert HEIC images to PNG')
    parser.add_argument('input_dir', help='input directory containing HEIC images')
    parser.add_argument('output_dir', help='output directory to save PNG images')
    args = parser.parse_args()

    # Convert images
    convert_images(args.input_dir, args.output_dir)
