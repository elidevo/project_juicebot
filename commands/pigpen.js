const { SlashCommandBuilder } = require('discord.js');
const { spawn } = require('child_process');
const { EmbedBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('pigpen')
		.setDescription('Converts a string into an image containing the corresponding pigpen cipher..')
		.addStringOption(option =>
			option.setName('input')
			.setDescription('The string to be converted into pigpen.')
			.setRequired(true)),
	async execute(interaction) {
		const strtoencrypt = interaction.options.getString('input');

		const child =  await spawn('python', ['./main.py', strtoencrypt], {shell: true});
		  
		await child.on('close', (code) => {
			interaction.channel.send({ files: [{ attachment: `./output.png`, name: 'output.png' }], });
			interaction.reply(":grapes:")
		});
	},
};
