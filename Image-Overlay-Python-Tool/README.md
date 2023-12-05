# Image Overlay Python Tool

## Overview

The Image Overlay Python Tool is a simple command-line utility that combines two images by overlaying their pixel values. The tool takes two input images and generates a new image where each pixel's RGB values are the sum of the corresponding pixels from the input images, modulo 256. This creates an overlay effect, blending the two images at a binary level.

## Features

- **Image Combination:** Overlay two images pixel by pixel to create a unique composite image.
- **Modulo 256 Arithmetic:** Ensure the resulting RGB values stay within the valid range (0-255).

## Usage

### Prerequisites

- Python 3.x
- Pillow library (`pip install Pillow`)

### Command Line

```bash
python overlay_images.py image1_path image2_path output_path
```

## Example

```bash
python overlay_images.py input_image1.jpg input_image2.png output_combined_image.jpg
```

# How It Works

The Image Overlay Python Tool follows a simple process to combine two images and create an overlay effect. Here's a step-by-step breakdown:

1. **Open the Input Images:**
   - The tool utilizes the Pillow library to open the two input images (`image1` and `image2`).

2. **Create a New Image:**
   - A new image is created with the same dimensions as the input images. This ensures that the overlay operation is performed on corresponding pixels.

3. **Combine Pixel Values:**
   - The tool iterates through each pixel in the input images.
   - For each pixel, it sums the RGB values from both images and takes the result modulo 256.
   - This step ensures that the combined RGB values stay within the valid range of 0 to 255.

4. **Save the Resulting Image:**
   - The final image, created by overlaying the input images, is saved to the specified output path.

This process results in a new image that represents the overlay of the two input images, providing a visually interesting combination of their pixel values.

Feel free to explore and experiment with different pairs of images to see the creative outcomes of this overlay operation!


## Contributing

Contributions are welcome! 

If you have suggestions, bug reports, or want to contribute to the codebase, feel free to open an issue or submit a pull request.
