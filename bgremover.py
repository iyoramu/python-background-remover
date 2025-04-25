MIT License

Copyright (c) 2025 IRUTABYOSE Yoramu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
import cv2
import numpy as np
from rembg import remove
from PIL import Image
import io
import argparse
import os

def remove_background(input_path, output_path):
    """
    Remove background from an image and save it with transparent background.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the output image with transparent background.
    """
    # Read the input image
    with open(input_path, 'rb') as f:
        input_image = f.read()
    
    # Remove the background
    output_image = remove(input_image)
    
    # Convert to PIL Image to handle transparency
    pil_image = Image.open(io.BytesIO(output_image))
    
    # Save the result
    pil_image.save(output_path, format='PNG')
    print(f"Background removed successfully! Result saved to {output_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Remove background from an image.')
    parser.add_argument('input_image', help='Path to the input image file')
    parser.add_argument('-o', '--output', help='Path to save the output image (default: input_image_without_bg.png)')
    
    args = parser.parse_args()
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        base_name = os.path.splitext(args.input_image)[0]
        output_path = f"{base_name}_without_bg.png"
    
    # Process the image
    remove_background(args.input_image, output_path)

if __name__ == "__main__":
    main()
