const { SlashCommandBuilder } = require("discord.js");
const { spawn } = require("child_process");
const { EmbedBuilder } = require("discord.js");
const { execSync } = require("child_process");

// https://discordjs.guide/slash-commands/parsing-options.html#subcommands
module.exports = {
	helpS2PText: `Usage: s2p STRING SCRAMBLED [OPTIONS]

  Returns an image of the supplied STRING and optionally SCRAMBLED.

Options:
	--color  The string corresponding to the color you want to use (case insensitive).`,

//////////////////////////////////////////////////////////////////////////

	helpS2EText: `Usage: s2e STRING SCRAMBLED

  Returns a sequence of pigpen emojis, created from the supplied STRING, and optionally SCRAMBLED.

Options:
	No options to show.`,

	data: new SlashCommandBuilder()
		.setName("pigpen")
		.setDescription("Converts a string into an image containing the corresponding pigpen cipher..")
		.addSubcommand(subcommand =>
			subcommand.setName("help")
			.setDescription("Help regarding this command")
			.addStringOption(option => 
				option.setName("mode")
				.setDescription("The mode to get information about")
				.setRequired(true)
				.addChoices(
					{name: "s2p", value: "s2p"},
					{name: "s2e", value: "s2e"},
					{name: "colors", value: "colors"}
				)
			)
		).addSubcommand(subcommand =>
			subcommand.setName("s2p")
			.setDescription("String to pigpen image.")
			.addStringOption(option =>
				option.setName("string")
				.setDescription("String to encode with pigpen")
				.setRequired(true)
			).addBooleanOption(option =>
				option.setName("scrambled")
				.setDescription("Scramble output?")
				.setRequired(true)
			).addStringOption(option =>
				option.setName("color")
				.setDescription("Color to make the text")
			)
		).addSubcommand(subcommand =>
			subcommand.setName("s2e")
			.setDescription("String to pigpen emojis.")
			.addStringOption(option =>
				option.setName("string")
				.setDescription("String to encode with pigpen")
				.setRequired(true)
			).addBooleanOption(option =>
				option.setName("scrambled")
				.setDescription("Scramble output?")
				.setRequired(true)
			)
		)
	,

	async execute(interaction) {
		const mode = interaction.options.getSubcommand();

		switch(mode){
		case "help":
			const submode = interaction.options.getString("mode");

			switch(submode){
			case "s2p":
				interaction.reply(this.helpS2PText);
				break;
			case "s2e":
				interaction.reply(this.helpS2EText);
				break;
			case "colors":
				const result = execSync("python ./main.py help colors");

				const child =  await spawn("python", ["./main.py", "help", "colors"], {shell: true}); // sheesh this is scary but i think its sanitized???
			
				await child.stdout.on('data', function(data) {
				    interaction.reply({ content: `Here are the available colors :grapes:\n\n${data.toString("utf8")}`, ephemeral: true });
				});

				break;
			default:
				interaction.reply("Invalid mode selection!");
				break;
			}

			break;
		case "s2p":
			const text = interaction.options.getString("string");
			const scramble = interaction.options.getBoolean("scrambled");
			const color = interaction.options.getString("color");

			const child =  await spawn("python", ["./main.py", "s2p", scramble, `"${text}"`, color], {shell: true}); // sheesh this is scary but i think its sanitized???
			child.stdout.on('data', function(data) {
			    // you can debug python program's stdout from here
			    console.log(`\nstdout: ${data}\n`)
			});
		  
			await child.on("close", (code) => {
				interaction.reply({ files: [{ attachment: `./output.png`, name: "output.png" }], content: "Here you go.. :grapes:\n\n", ephemeral: false })
			});

			break;
		case "s2e":
			const input = interaction.options.getString("string"); // why are cases in the same scope???!?????
			const scrambled = interaction.options.getBoolean("scrambled");

			const mchild =  await spawn("python", ["./main.py", "s2e", scrambled, `"${input}"`], {shell: true}); // sheesh this is scary but i think its sanitized???
			mchild.stdout.on('data', function(data) {
			    // you can debug python program's stdout from here
			    console.log(`stdout: ${data}`)

			    interaction.reply({ content: `Here you go.. :grapes:\n\n${data}`, ephemeral: false })
			});

			break;
		default:
			break;
		}
	}
};