const { SlashCommandBuilder } = require("discord.js");
const { spawn } = require("child_process");
const { EmbedBuilder } = require("discord.js");
const { execSync } = require("child_process");

// https://discordjs.guide/slash-commands/parsing-options.html#subcommands
module.exports = {
	data: new SlashCommandBuilder()
		.setName("pigpenimage")
		.setDescription("Converts a string into an image containing the corresponding pigpen cipher..")
		.addStringOption(option =>
			option.setName("string")
			.setDescription("String to encode with pigpen")
			.setRequired(true)
		).addBooleanOption(option =>
			option.setName("scrambled")
			.setDescription("Scramble the output?")
			.setRequired(true)
		).addStringOption(option =>
			option.setName("color")
			.setDescription("Color to make the output text within the image.")
		)
	,

	async execute(interaction) {
		const string = interaction.options.getString("string")
		const color = interaction.options.getString("color") || "WHITE"
		const scrambled = interaction.options.getBoolean("scrambled")

		const child =  await spawn("python", ["./main.py", "s2p", scrambled, `"${string}"`, color], {shell: true}); // sheesh this is scary but i think its sanitized???
		child.stdout.on('data', function(data) {
		    // you can debug python program's stdout from here
		    console.log(`\nstdout: ${data}\n`)
		});
	  
		await child.on("close", (code) => {
			interaction.reply({ files: [{ attachment: `./output.png`, name: "output.png" }], content: "Here you go.. :grapes:\n\n", ephemeral: false })
		});
	}
};