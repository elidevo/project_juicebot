from PIL import Image
from random import shuffle
from math import ceil

import re, os, sys

# A map of the emojis on the server, could add some cool functionality in future?
# does discord.js allow me to create guild emojis on a bot?
alphabet = {
	" ": " ",
	"a": ":XKav_1:",
	"b": ":IIRC_2:",
	"c": ":xRTk_3:",
	"d": ":ZjJm_4:",
	"e": ":ryCZ_5:",
	"f": ":vvCD_6:",
	"g": ":VXC4_7:",
	"h": ":41Aj_8:",
	"i": ":cQ8L_9:",
	"j": ":uD7D_10:",
	"k": ":BNdj_11:",
	"l": ":hwHj_12:",
	"m": ":dbRq_13:",
	"n": ":V9UP_14:",
	"o": ":nLI6_15:",
	"p": ":u69l_16:",
	"q": ":DKfP_17:",
	"r": ":ov3n_18:",
	"s": ":cU2N_19:",
	"t": ":xrt3_20:",
	"u": ":ZtsP_21:",
	"v": ":qBHD_22:",
	"w": ":n8um_23:",
	"x": ":2U27_24:",
	"y": ":hjdL_25:",
	"z": ":6XYb_26:"
}

# Converts characters to discord emojis, translating to pigpen
# time complexity = O(n)
# space complexity = ???
def text_to_pigpen(text):
	strng = ""

	try:
		for letter in text:
			strng = strng + str(alphabet[letter]) + " "
	except:
		pass

	return strng[0:len(strng) - 1]

# Scrambles discord emojis already in pigpen
# time complexity = O(n)
# space complexity = ???
def pigpen_scramble(pigpen):
	arr = pigpen.split(" ")
	shuf = [n for n in arr if n != ""]

	shuffle(shuf)

	return " ".join(shuf)

# Converts text to pigpen images
# time complexity = O(n)
# space complexity = ????
def text_to_pigpen_image(filename, text):
	regex = re.compile('[^a-zA-Z]')
	regex.sub("", text)

	maxcharwidth = 30 # maximum characters allowed on a row before going to the next
	imgwidth = 30 # donot modify, this is image width/height


	width = imgwidth*len(text) # width of host image
	height = imgwidth*ceil(len(text)/maxcharwidth) # height of host image

	if len(text) > maxcharwidth: # if the text is too long, and wraps then let's adjust the width of the cipher image
		width = imgwidth*maxcharwidth

	img = Image.new(mode="RGBA", size=(width, height), color = (90, 90, 255, 0)) # declare cipher "host image"

	# emplace cipher characters onto host image in a loop | O(n)
	x, y = 0, 0
	for letter in text:
		if letter.isalpha():
			img2 = Image.open("./images/pigpen_alphabet/" + letter + '.png') # make this based off os.cwd
			img2.convert("RGBA")
			img.paste(img2, ((0 + (x * imgwidth), y*imgwidth)), img2)

		x = x + 1
		if x == maxcharwidth:
			x = 0
			y = y + 1

	img.save(filename + ".png") # save final host image

	# might use this to pipe the filename to the bot instead of how it's done now
	print("{}\\{}.png".format(os.getcwd(), filename))


# main function
def main():
	try:
		text_to_pigpen_image("output", " ".join(sys.argv[1::]))
	except:
		pass


# entrypoint
if __name__ == '__main__':
    main()