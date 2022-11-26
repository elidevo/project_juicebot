const { SlashCommandBuilder } = require("discord.js");
const { spawn } = require("child_process");
const { EmbedBuilder } = require("discord.js");
const { execSync } = require("child_process");

// https://discordjs.guide/slash-commands/parsing-options.html#subcommands
module.exports = {
	data: new SlashCommandBuilder()
		.setName("pigpenemoji")
		.setDescription("Converts a string into an image containing the corresponding pigpen cipher..")
		.addStringOption(option =>
			option.setName("string")
			.setDescription("String to encode with pigpen")
			.setRequired(true)
		).addBooleanOption(option =>
			option.setName("scrambled")
			.setDescription("Scramble the output?")
			.setRequired(true)
		)
	,

	async execute(interaction) {
		const string = interaction.options.getString("string");
		const scrambled = interaction.options.getBoolean("scrambled");

		const mchild =  await spawn("python", ["./main.py", "s2e", scrambled, `"${string}"`], {shell: true}); // sheesh this is scary but i think its sanitized???
		mchild.stdout.on('data', function(data) {
		    // you can debug python program's stdout from here
		    console.log(`stdout: ${data}`)

		    interaction.reply({ content: `Here you go.. :grapes:\n\n${data}`, ephemeral: false })
		});
	}
};