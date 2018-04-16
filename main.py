from PIL import Image
from sys import argv

def numberinput(question, mustbemultipleofonefifth):
	success = False
	while success == False:
		success = True
		try:
			out = float(raw_input(question))
		except:
			success = False
			print 'Not a valid number'
	if mustbemultipleofonefifth:
		return round(out/.2)*.2
	else:
		return out

output = ''
imgsuccess = False
if len(argv) >= 2:
	try: 
		im = Image.open(argv[1])
		imgsuccess = True
	except:
		print 'Image "' + argv[1] + '" not found'
else:
	print 'No image given'
	
if imgsuccess:
	pix = im.load()
	width, height = im.size

	output += str(numberinput('How far up should the top of the course be (1px = .2 units)?\n>>> ', True)) + '\n'
	output += str(numberinput('What is the lowest y value the player can be?\n>>> ', False)) + '\n'
	output += str(numberinput('What is the highest y value the player can be?\n>>> ', False)) + '\n'
	output += str(numberinput('How far does the player need to be to win?\n>>> ', False))

	for i in range(height):
		output += '\n'
		for j in range(width):
			if (pix[j, i] == (0, 0, 0, 255)):
				output += '1'
			else:
				output += '0'
	print "Here is your file:"
	with open(argv[1].split('.')[0]+'.alg', 'w') as f:
		f.write(output)
