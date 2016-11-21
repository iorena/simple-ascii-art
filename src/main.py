import cv2 
import sys
import asciifier

def main():
	try:
		image = cv2.imread(sys.argv[1])
	except:
		print 'Error reading image.'
		sys.exit(0)
	print asciifier.asciify(image)


if __name__ == '__main__':
	main()
