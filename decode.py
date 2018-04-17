from PIL import Image
import numpy as np
import sys

def toEnglish(asciiList):
	message = ''
	for eachAscii in asciiList:
		alphabet = chr(int(eachAscii,2))
		message += alphabet
		
	return message



def main():
	if(len(sys.argv) == 1):
		imgPath = input("Enter path of Image :\n> ")
	else:
		imgPath = sys.argv[1]

	try:
		img = Image.open(imgPath)
	except Exception as e:
		print(e)
		print("Try Again..")
		main()
	print("Decoding..\n")
	
	arr = np.array(img)

	pix = ''
	listOfAscii = []
	pixOver = 0
	finish = False

	for row in arr:
		for column in row:
			binPix = "{0:08b}".format(column)
			if (pixOver == 4):
				if(pix == '01100000'): #terminator
					finish = True
					break
				listOfAscii.append(pix)
				pix = ''
				pixOver = 0
			binPix = "{0:08b}".format(column)
			pixEnding = binPix[-2:]
			pix += pixEnding
			pixOver += 1

		if(finish):
			break
	

	msg = toEnglish(listOfAscii)
	print("Message :")
	msg = msg.replace("\\n","\n")
	print(msg)


if __name__ == "__main__":
	main()
