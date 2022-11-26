const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('juice')
		.setDescription('sipping juice 4 life.'),
	async execute(interaction) {
		await interaction.reply('we sipping juice 4 life buddy');
	},
};