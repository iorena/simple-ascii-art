from __future__ import division
import cv2 

#todo: make module into object

def asciify(image):
	getBlockSize(image)
	return 0

#if image aspect ratio is different from our 36x12 chars ratio, make ascii area smaller
def getBlockSize(image):
	maxY = 12
	maxX = 36
	ratio = 1.5
	stepX = None
	stepY = None
	img = None
	img = image
	imgX = img.shape[1]
	imgY = img.shape[0]
	print imgX
	print imgY
	imgRatio = imgX / imgY
	print imgRatio
	if imgRatio > 1.5:
		maxY = int(maxX * imgRatio / 2)
	if imgRatio < 1.5:
		maxX = int(maxY * imgRatio * 2)
	print maxX
	print maxY

	stepX = int(imgX / maxX)
	stepY = int(imgY / maxY)
	print stepX * maxX
	print stepY * maxY


def getBlock(x, y):
	return 0
	#return cv2.getSubRect(x * 
