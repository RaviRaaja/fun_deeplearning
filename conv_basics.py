# import the necessary packages
from skimage.exposure import rescale_intensity
import numpy as np
import cv2
import argparse
import sys

# construct a sharpening filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

# construct the Laplacian kernel used to detect edge-like
# regions of an image
laplacian1 = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

laplacian2 = np.array((
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]), dtype="int")

# construct the Sobel x-axis kernel
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

# construct the kernel bank, a list of kernels we're going
# to apply using both our custom `convole` function and
# OpenCV's `filter2D` function
kernelBank = {
"sharpen": sharpen,
"laplacian1": laplacian1,
"laplacian2":laplacian2,
"sobel_x": sobelX,
"sobel_y": sobelY
}



def convolve(image, kernel):
    # grab the spatial dimensions of the image, along with
    # the spatial dimensions of the kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    # allocate memory for the output image, taking care to
    # "pad" the borders of the input image so the spatial
    # size (i.e., width and height) are not reduced
    pad = int((kW - 1) / 2)
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    
    # loop over the input image, "sliding" the kernel across
    # each (x, y)-coordinate from left-to-right and top to
    # bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract the ROI of the image by extracting the
            # *center* region of the current (x, y)-coordinates
            # dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            # perform the actual convolution by taking the
            # element-wise multiplicate between the ROI and
            # the kernel, then summing the matrix
            k = (roi * kernel).sum()

            # store the convolved value in the output (x,y)-
            # coordinate of the output image
            output[y - pad, x - pad] = k
            
    # rescale the output image to be in the range [0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    
    # return the output image
    return output

def main(args):
    # load the input image and convert it to grayscale
    print("AVAILABLE CONV KERNELS OF SIZE (3,3)")
    for key, value in kernelBank.items() :
        print (key)

    kernelName = input("Enter KernelName to convolve image with - ")

    #experimenting on image1
    image = cv2.imread(args.image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("[INFO] applying {} kernel".format(kernelName))
    convoleOutput = convolve(gray, kernelBank[kernelName])
    opencvOutput = cv2.filter2D(gray, -1, kernelBank[kernelName])
    cv2.imshow("after opncv - CONV",opencvOutput)
    cv2.imshow("after my conv  - CONV",convoleOutput)
    cv2.imshow("before CONV",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, help='Path to image of type jpg or png')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    