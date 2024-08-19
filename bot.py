import os
import discord
from discord.ext import commands
from discord import app_commands
from views import LanguageDropdownView
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DevsCertified"

DISCORD_TOKEN = os.getenv('token')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Needed to access guilds

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

# Command to list all servers the bot is in
@bot.tree.command(name="list", description="List all servers the bot is in")
async def list_guilds(interaction: discord.Interaction):
    guilds = bot.guilds
    guild_list = "\n".join([f"{guild.name} (ID: {guild.id})" for guild in guilds])
    
    if guild_list:
        await interaction.response.send_message(f"Bot is in the following servers:\n{guild_list}")
    else:
        await interaction.response.send_message("The bot is not in any servers.")

# Command to make the bot leave a server by ID, restricted to a specific user
@bot.tree.command(name="leave", description="Make the bot leave a server by ID")
@app_commands.describe(guild_id="ID of the server to leave")
async def leave_guild(interaction: discord.Interaction, guild_id: int):
    allowed_user_id = 936320442594103307  # User ID allowed to use the command

    if interaction.user.id != allowed_user_id:
        await interaction.response.send_message("You do not have permission to use this command.")
        return

    guild = discord.utils.get(bot.guilds, id=guild_id)
    
    if guild:
        await guild.leave()
        await interaction.response.send_message(f"Bot has left the server: {guild.name}")
    else:
        await interaction.response.send_message("Guild ID not found or the bot is not in that guild.")

def run_discord_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8000, 'debug': False})
    flask_thread.start()
    
    # Run the Discord bot in the main thread
    run_discord_bot()
