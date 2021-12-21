# USAGE
# python simple.py --image images/moon.png

import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the input image from disk and convert it to grayscale
print("[INFO] loading image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] equalizing histogram...")
equalized = cv2.equalizeHist(gray)

# show the original and equalized image
cv2.imshow("Input", gray)
cv2.imshow("Equalized", equalized)
cv2.waitKey(0)

