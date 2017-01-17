from __future__ import division
import cv2 

class Asciifier:

	def __init__(self):
		self.maxY = 12
		self.maxX = 30
		self.fontRatio = 0.59
		self.ratio = self.fontRatio * self.maxX / self.maxY
		print self.ratio
		self.stepX = None
		self.stepY = None
		self.img = None
		self.letters = [' ', '\\','/','-','(',')','\'',',','[','"','"','#','.',':',';','^','>',']','<','@','1','l','L','I','v','Y','y','V','T','t','|','_']
		self.samples = [None] * 32

	def asciify(self, image):
		self.getBlockSize(image)
		self.img = cv2.Canny(self.img, 170, 200)
		self.loadSamples()
		self.chars = ''
		cv2.imshow('', self.img)
		cv2.waitKey(0)
		#match each block with an ascii char
		for x in range(0, self.maxX):
			for y in range(0, self.maxY):
				block = self.getBlock(x, y)
				self.chars += self.getAscii(block)
		#add line breaks
		for x in range(0, self.maxY):
			self.chars = self.chars[:self.maxX*(x+1)+x] + '\n' + self.chars[self.maxX*(x+1)+x:]
		return self.chars

	#if image aspect ratio is different from our 40x12 chars ratio, make ascii area smaller to match
	def getBlockSize(self, image):
		self.img = image
		imgX = self.img.shape[1]
		imgY = self.img.shape[0]
		imgRatio = imgX / imgY
		if imgRatio > self.ratio:
			self.maxY = int(self.maxX * imgRatio * self.fontRatio)
		if imgRatio < self.ratio:
			self.maxX = int(self.maxY * imgRatio / self.fontRatio)
		print self.maxX
		print self.maxY

		self.stepX = int(imgX / self.maxX)
		self.stepY = int(imgY / self.maxY)
		print self.stepX * self.maxX
		print self.stepY * self.maxY


	def getBlock(self, x, y):
		x = x * self.stepX
		y = y * self.stepY
		return self.img[y:(y + self.stepY),x:(x + self.stepX)]

	def loadSamples(self):
		for n in range(1,32):
			self.samples[n-1] = cv2.imread('letter'+str(n)+'.jpg', 0)


	#compare char sized block to sample images
	def getAscii(self, block):
		angles = 11
		results = [[] for i in range(32)] 
		for x in range(0, 31):
			sample = self.samples[x]
			sample = cv2.resize(sample, (self.stepX, self.stepY))
			rotResults = []
			for y in range(1, angles):
				angle = y * 5 - 30
				rotatedSample = self.rotate(sample, angle)
				#cv2.imshow("rotated", rotatedSample)
				#cv2.waitKey(0)
				res = cv2.matchTemplate(block, rotatedSample, 0)
				min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
				rotResults.append(min_val)
			#if min_val != 0.0:
				#print min_val, max_val, x
			results[x] = min(rotResults)


		index = results.index(min(results))
		#print index
		return self.letters[index]

	#returns rotated image
	def rotate(self, source, angle):
		center = (self.stepX / 2, self.stepY / 2)
		rot = cv2.getRotationMatrix2D(center, angle, 1.0)
		rotated = cv2.warpAffine(source, rot, (self.stepX, self.stepY))
		return rotated
