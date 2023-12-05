from PIL import Image
import argparse
import sys

def combine_images(image1_path, image2_path, output_path):
    # Opening the two input images
    img1 = Image.open(image1_path)
    pixels1 = img1.load()
    img2 = Image.open(image2_path)
    pixels2 = img2.load()

    # Creating a new image for the final result with the same size as of the input images
    width, height = img1.size
    flag = Image.new("RGB", (width, height))
    flagpix = flag.load()

    # Combining the pixel values from the two input images
    for row in range(height):
        for col in range(width):
            flagpix[col, row] = (
                (pixels1[col, row][0] + pixels2[col, row][0]) % 256,
                (pixels1[col, row][1] + pixels2[col, row][1]) % 256,
                (pixels1[col, row][2] + pixels2[col, row][2]) % 256,
            )

    # Saving the final image
    flag.save(output_path)

    # Printing a success message
    print("\n"+"Operation Successful!!"+"\n")
    print(f"Overlaid {image1_path} and {image2_path} successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine two images into one.")
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    parser.add_argument("output", help="Path for the output image")

    args = parser.parse_args()

    if len(sys.argv) != 4:
        parser.print_usage()
    else:
        combine_images(args.image1, args.image2, args.output)
