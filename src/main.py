import cv2 
import sys
from asciifier import Asciifier

def main():
	try:
		image = cv2.imread(sys.argv[1], 0)
	except:
		print 'Error reading image.'
		sys.exit(0)
	asciifier = Asciifier()
	print asciifier.asciify(image)


if __name__ == '__main__':
	main()
