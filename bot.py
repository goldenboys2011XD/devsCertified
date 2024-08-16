import discord
from discord.ext import commands
from discord import app_commands
from views import LanguageDropdownView
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')
    await bot.tree.sync()

@bot.tree.command(name="certificated", description="Get certified in a programming language")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Select a programming language to start the quiz:",
        view=LanguageDropdownView())

bot.run(DISCORD_TOKEN)
