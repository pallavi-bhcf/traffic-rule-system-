# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from spectrumtech.colordescriptor import ColorDescriptor
from spectrumtech.searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
print(args)
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))
print(cd)
# load the query image and describe it
query = cv2.imread(args["query"])
cv2.imshow("Query", query)
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
results=results[0:1]
for i in results:
    print(i)

#display the query
cv2.imshow("Query", query)

# loop over the results
for (score, resultID) in results:
 	# load the result image and display it
 	result = cv2.imread(resultID)
 	cv2.imshow("Result", result)
 	cv2.waitKey(0)