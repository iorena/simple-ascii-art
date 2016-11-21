from __future__ import division
import cv2 

#todo: make module into object

class Asciifier:

	def __init__(self):
		self.maxY = 12
		self.maxX = 36
		self.ratio = 1.5
		self.stepX = None
		self.stepY = None
		self.img = None

	def asciify(self, image):
		self.getBlockSize(image)
		return 0

	#if image aspect ratio is different from our 36x12 chars ratio, make ascii area smaller
	def getBlockSize(self, image):
		self.img = image
		imgX = self.img.shape[1]
		imgY = self.img.shape[0]
		print imgX
		print imgY
		imgRatio = imgX / imgY
		print imgRatio
		if imgRatio > self.ratio:
			self.maxY = int(self.maxX * imgRatio / 2)
		if imgRatio < self.ratio:
			self.maxX = int(self.maxY * imgRatio * 2)
		print self.maxX
		print self.maxY

		self.stepX = int(imgX / self.maxX)
		self.stepY = int(imgY / self.maxY)
		print self.stepX * self.maxX
		print self.stepY * self.maxY


	def getBlock(self, x, y):
		return 0
		#return cv2.getSubRect(x * 
