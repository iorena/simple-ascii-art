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
		self.img = cv2.Canny(self.img, 200, 200)
		self.loadSamples()
		self.chars = ''
		#match each block with an ascii char
		for x in range(0, self.maxX):
			for y in range(0, self.maxY):
				block = self.getBlock(x, y)
				#cv2.imshow('', block)
				#cv2.waitKey(0)
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


	def getAscii(self, block):
		results = [None] * 32
		for x in range(0,31):
			sample = self.samples[x]
			sample = cv2.resize(sample, (self.stepX, self.stepY))
			#print 'x', x, sample.shape[1], block.shape[1]
			#print 'y', x, sample.shape[0], block.shape[0]
			res = cv2.matchTemplate(block, sample, 5)
			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
			if min_val != 0.0:
				print min_val, max_val, x
			results[x] = max_val
		index = results.index(max(results))
		#print index
		return self.letters[index]
