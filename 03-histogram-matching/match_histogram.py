from skimage import exposure
import matplotlib.pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True, help="Path to the source image")
ap.add_argument("-r", "--reference", required=True, help="Path to the reference image")
args = vars(ap.parse_args())

# load the source and reference images
print("[INFO] loading images...")
source = cv2.imread(args["source"])
reference = cv2.imread(args["reference"])

# determine if we are performing multichanner histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
# multi = True if source.shape[-1] > 1 else False
matched = exposure.match_histograms(source, reference, multichannel=True)

# show the output images
cv2.imshow("Source", source)
cv2.imshow("Reference", reference)
cv2.imshow("Matched", matched)
cv2.waitKey(0)

