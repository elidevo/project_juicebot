from PIL import Image
from random import shuffle, randint
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

# dictionary of colors
colors = {
	"RED": (255, 0, 0),
	"GREEN": (0, 255, 0),
	"BLUE": (0, 0, 255),
	# SHADES,
	"BLACK": (0, 0, 0),
	"DARK_GREY": (60, 60, 60),
	"DARK_SLATE_GREY": (47, 79, 79),
	"DIM_GREY": (105, 105, 105),
	"FREE_SPEECH_GREY": (99, 86, 136),
	"GREY": (190, 190, 190),
	"GREY0": (0, 0, 0),
	"GREY1": (3, 3, 3),
	"GREY2": (5, 5, 5),
	"GREY3": (8, 8, 8),
	"GREY32": (82, 82, 82),
	"GREY33": (84, 84, 84),
	"GREY34": (87, 87, 87),
	"GREY35": (89, 89, 89),
	"GREY36": (92, 92, 92),
	"GREY37": (94, 94, 94),
	"GREY38": (97, 97, 97),
	"GREY39": (99, 99, 99),
	"GREY40": (102, 102, 102),
	"GREY41": (105, 105, 105),
	"GREY42": (107, 107, 107),
	"GREY43": (110, 110, 110),
	"GREY44": (112, 112, 112),
	"GREY45": (115, 115, 115),
	"GREY46": (117, 117, 117),
	"GREY47": (120, 120, 120),
	"GREY48": (122, 122, 122),
	"GREY62": (158, 158, 158),
	"GREY63": (161, 161, 161),
	"GREY64": (163, 163, 163),
	"GREY96": (245, 245, 245),
	"GREY97": (247, 247, 247),
	"GREY98": (250, 250, 250),
	"GREY99": (252, 252, 252),
	"LIGHT_GREY": (211, 211, 211),
	"SLATE_GREY": (112, 128, 144),
	"SLATE_GREY_3": (159, 182, 205),
	"VERY_LIGHT_GREY": (205, 205, 205),
	"WHITE": (255, 255,255),
	 
	"ALICE_BLUE": (240, 248, 255),
	"AQUA": (0, 255, 255),
	"AQUAMARINE": (127, 255, 212),
	"AQUAMARINE_3": (102, 205, 170),
	"AZURE": (240, 255, 255),
	"AZURE_3": (193, 205, 205),
	"BLUE_3": (0, 0, 205),
	"BLUE_VIOLET": (138, 43, 226),
	"CADET_BLUE": (95, 159, 159),
	"CADET_BLUE_3": (122, 197, 205),
	"CORN_FLOWER_BLUE": (66, 66, 111),
	"CYAN": (0, 255, 255),
	"CYAN_3": (0, 205, 205),
	"DARK_SLATE_BLUE": (36, 24, 130),
	"DARK_TURQUOISE": (112, 147, 219),
	"DEEP_SKY_BLUE": (0, 191, 255),
	"DEEP_SKY_BLUE_3": (0, 154, 205),
	"DODGER_BLUE": (30, 144, 255),
	"DODGER_BLUE_3": (24, 116, 205),
	"FREE_SPEECH_BLUE": (65, 86, 197),
	"LIGHT_BLUE": (173, 216, 230),
	"LIGHT_SLATE_BLUE": (132, 112, 255),
	"LIGHT_STEEL_BLUE": (176, 196, 222),
	"LIGHT_STEEL_BLUE_3": (162, 181, 205),
	"MEDIUM_BLUE": (0, 0, 205),
	"MEDIUM_SLATE_BLUE": (123, 104, 238),
	"MEDIUM_TURQUOISE": (72, 209, 204),
	"MIDNIGHT_BLUE": (25, 25, 112),
	"NAVY": (0, 0, 128),
	"NAVY_BLUE": (0, 0, 128),
	"NEON_BLUE": (77, 77, 255),
	"NEW_MIDNIGHT_BLUE": (0, 0, 156),
	"PALE_TURQUOISE": (187, 255, 255),
	"PALE_TURQUOISE_3": (150, 205, 205),
	"POWDER_BLUE": (176, 224, 230),
	"RICH_BLUE": (89, 89, 171),
	"ROYAL_BLUE": (65, 105, 225),
	"ROYAL_BLUE_3": (58, 95, 205),
	"ROYAL_BLUE_5": (0, 34, 102),
	"SKY_BLUE": (135, 206, 235),
	"SKY_BLUE_3": (108, 166, 205),
	"SLATE_BLUE": (131, 111, 255),
	"SLATE_BLUE_3": (105, 89, 205),
	"STEEL_BLUE": (70, 130, 180),
	"STEEL_BLUE_3": (79, 148, 205),
	"SUMMER_SKY": (56, 176, 222),
	"TEAL": (0, 128, 128),
	"TRUE_IRIS_BLUE": (3, 180, 204),
	"TURQUOISE": (64, 224, 208),
	"TURQUOISE_3": (0, 197, 205),
	 
	 
	"BAKERS_CHOCOLATE": (92, 51, 23),
	"BEIGE": (245, 245, 220),
	"BROWN": (166, 42, 42),
	"BROWN_3": (205, 51, 51),
	"BURLYWOOD": (222, 184, 135),
	"BURLYWOOD_3": (205, 170, 125),
	"NEW_TAN": (235, 199, 158),
	"PERU": (205, 133, 63),
	"ROSY_BROWN": (188, 143, 143),
	"ROSY_BROWN_3": (205, 155, 155),
	"SADDLE_BROWN": (139, 69, 19),
	"SANDY_BROWN": (244, 164, 96),
	"SEMI_SWEET_CHOCOLATE": (107, 66, 38),
	"SIENNA": (142, 107, 35),
	"TAN": (219, 147, 112),
	"TAN_3": (205, 133, 63),
	"VERY_DARK_BROWN": (92, 64,51),
	 
	"CHARTREUSE": (127, 255, 0),
	"CHARTREUSE_3": (102, 205, 0),
	"DARK_GREEN": (47, 79, 47),
	"DARK_GREEN_COPPER": (74, 118, 110),
	"DARK_KHAKI": (189, 183, 107),
	"DARK_OLIVE_GREEN": (85, 107, 47),
	"DARK_OLIVE_GREEN_3": (162, 205, 90),
	"DARK_SEA_GREEN": (143, 188, 143),
	"DARK_SEA_GREEN_3": (155, 205, 155),
	"FOREST_GREEN": (34, 139, 34),
	"FREE_SPEECH_GREEN": (9, 249, 17),
	"GREEN_3": (0, 205, 0),
	"SEA_GREEN_3": (67, 205, 128),
	"SPRING_GREEN": (0, 255, 127),
	"SPRING_GREEN_3": (0, 205, 102),
	"YELLOW_GREEN": (154, 205,50),
	 
	 
	"BISQUE": (255, 228, 196),
	"BISQUE_3": (205, 183, 158),
	"LIGHT_CORAL": (240, 128, 128),
	"LIGHT_SALMON": (255, 160, 122),
	"LIGHT_SALMON_3": (205, 129, 98),
	"MANDARIN_ORANGE": (142, 35, 35),
	"ORANGE": (255, 165, 0),
	"ORANGE_3": (205, 133, 0),
	"ORANGE_RED": (255, 36, 0),
	"PEACH_PUFF": (255, 218, 185),
	"PEACH_PUFF_3": (205, 175, 149),
	"SALMON": (250, 128, 114),
	"SALMON_3": (205, 112, 84),
	"TOMATO_3": (205, 79, 57),
	"VIOLET_RED": (208, 32, 144),
	"VIOLET_RED_3": (205, 50, 120),
	 
	"DARK_ORCHID": (153, 50, 204),
	"DARK_ORCHID_3": (154, 50, 205),
	"DARK_PURPLE": (135, 31, 120),
	"DARK_VIOLET": (148, 0, 211),
	"FUCHSIA": (255, 0, 255),
	"LAVENDER": (230, 230, 250),
	"LAVENDER_BLUSH": (255, 240, 245),
	"LAVENDER_BLUSH_3": (205, 193, 197),
	"MAGENTA": (255, 0, 255),
	"MAGENTA_3": (205, 0, 205),
	"MAROON": (176, 48, 96),
	"PURPLE_3": (125, 38, 205),
	"THISTLE": (216, 191, 216),
	"THISTLE_3": (205, 181, 205),
	"VIOLET": (238, 130, 238),
	"VIOLET_BLUE": (159, 95, 159),
	"BLANCHED_ALMOND": (255, 235, 205),
	"SNOW": (255, 250, 250),
	"SNOW_3": (205, 201, 201),
	"WHEAT": (245, 222, 179),
	"WHEAT_3": (205, 186, 150),
	"QUARTZ": (217, 217, 243) 
}

# Converts characters to discord emojis, translating to pigpen
# time complexity = O(n)
# space complexity = ???
def text_to_pigpen(text):
	ret = ""
	
	regex = re.compile('[^a-zA-Z]')
	regex.sub("", text)

	for letter in text:
		ret = ret + str(alphabet[letter]) + " "

	return ret[0:len(ret) - 1]

# Scrambles discord emojis already in pigpen
# time complexity = O(n)
# space complexity = ???
def text_scramble(text):
	shuf = [n for n in text]
	shuffle(shuf)

	return "".join(shuf)

# Converts text to pigpen images
# time complexity = O(n)
# space complexity = ????
def text_to_pigpen_image(filename, text, col="WHITE"):
	regex = re.compile('[^a-zA-Z]')
	regex.sub("", text)

	maxcharwidth = 30 # maximum characters allowed on a row before going to the next
	imgwidth = 30 # DO NOT MODIFY, this is image width/height

	width = imgwidth*len(text) # width of host image
	height = imgwidth*ceil(len(text)/maxcharwidth) # height of host image

	if len(text) > maxcharwidth: # if the text is too long, and wraps then let's adjust the width of the cipher image
		width = imgwidth*maxcharwidth

	img = Image.new(mode="RGBA", size=(width, height), color = (90, 90, 255, 0)) # initialize cipher "host image"

	# emplace cipher characters onto host image in a loop | O(n)
	x, y = 0, 0
	for letter in text:
		try:
			img2 = Image.open("./images/pigpen_alphabet/" + letter + '.png') # make this based off os.cwd
			img2.convert("RGBA")

			# Code for dynamically changing font color.
			new_img = []
			coltup = colors[col.upper()]
			for item in img2.getdata():
				bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
				new_img.append(coltup + (item[3],))

			img2.putdata(new_img)
			img.paste(img2, ((0 + (x * imgwidth), y*imgwidth)), img2)
		except:
			print("Error opening/handling alphabet character image.")

		x = x + 1
		if x == maxcharwidth:
			x = 0
			y = y + 1

	img.save(filename + ".png") # save final host image

	# might use this to pipe the filename to the bot instead of how it's done now
	print("{}\\{}.png".format(os.getcwd(), filename))

# main function
# TODO: FIGURE OUT HOW TO CORRECTLY DO ERROR HANDLING SO IT CAN BE REPORTED TO THE FRONT
def main():
	try:
		mode = sys.argv[1]
		if mode not in ["s2p", "s2e", "help"]:
			print("Incorrect mode supplied")

			return 1;
		if mode.lower() == "help":
			try:
				submode = sys.argv[2]
				if submode not in ["colors"]:
					print("Incorrect submode supplied")

					return 1;
			except:
				print("No submode supplied")

				return 1;

			match submode:
				case "colors":
					print(", ".join(colors.keys()))

					return 0;
				case _:
					pass
		elif mode.lower() == "s2p":
			try:
				scramble = sys.argv[2]
				text = sys.argv[3]
				color = "WHITE"
				
				if len(sys.argv) == 5 and sys.argv[4].upper() in colors.keys():
					color = sys.argv[4].upper()

				scramble = scramble.lower() == "true"

				if scramble:
					text = text_scramble(text)

				return text_to_pigpen_image("output", text, col=color)
			except:
				print("Incorrect call")

				return 1;
					
		elif mode.lower() == "s2e":
			try:
				scramble = sys.argv[2]
				text = sys.argv[3]
			except:
				print("Error in s2e...")

			scramble = scramble.lower() == "true"

			if scramble:
				text = text_scramble(text)

			print(text_to_pigpen(text))
	except:
		return 1;

	return 0;

# entrypoint
if __name__ == '__main__':
    main()