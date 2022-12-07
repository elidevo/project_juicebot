const { SlashCommandBuilder } = require("discord.js");
const { spawn } = require("child_process");
const { EmbedBuilder } = require("discord.js");
const { execSync } = require("child_process");

const alphabetl = "abcdefghijklmnopqrstuvwxyz"
const alphabetu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

function stringToCeasar(string, offset, scrambled){
	var str = ""

	for(var i = 0; i < string.length; i++){
		const charCode = string.charCodeAt(i)
		const char = string[i]

		if(alphabetl.includes(char) || alphabetu.includes(char)){
			if(char == char.toUpperCase()){
				str = str + alphabetu[((charCode - 65) + offset % alphabetl.length + alphabetl.length) % alphabetu.length]
			}else if(char == char.toLowerCase()){
				str = str + alphabetl[((charCode - 97) + offset % alphabetl.length + alphabetl.length) % alphabetl.length]
			}
		}else{
			str = str + char
		}
	}

	return scrambled ? str.split('').sort(function(){return 0.5-Math.random()}).join('') : str;
}


// https://discordjs.guide/slash-commands/parsing-options.html#subcommands
module.exports = {
	data: new SlashCommandBuilder()
		.setName("caesar")
		.setDescription("Converts a string into an image containing the corresponding pigpen cipher..")
		.addStringOption(option =>
			option.setName("string")
			.setDescription("String to be converted into pigpen.")
			.setRequired(true)
		).addBooleanOption(option =>
			option.setName("scrambled")
			.setDescription("Should the output be scrambled?")
			.setRequired(true)
		).addIntegerOption(option =>
			option.setName("offset")
			.setDescription("How much to offset the input by? 1-25")
			.setMinValue(1)
			.setMaxValue(25)
			.setRequired(true)
		)
	,

	async execute(interaction) {
		const string = interaction.options.getString("string")
		const scrambled = interaction.options.getBoolean("scrambled")
		const offset = interaction.options.getInteger("offset")

		await interaction.reply(`Here you go.. :grapes:\n\n${stringToCeasar(string, offset, scrambled)}`);

	}
};