import os
import discord
from discord.ext import commands
from discord import app_commands
from views import LanguageDropdownView
from flask import Flask
import threading

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DevsCertified"

# Get the bot token from environment variables
DISCORD_TOKEN = os.getenv('token')

# Create a bot instance with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Your Discord user ID (for restricting command access)
OWNER_ID = 936320442594103307

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')
    await bot.tree.sync()  # Sync slash commands with Discord

@bot.tree.command(name="certificated", description="Get certified in a programming language")
async def slash_certificated(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Select a programming language to start the quiz:",
        view=LanguageDropdownView())

@bot.tree.command(name="list", description="List all servers the bot is in")
async def slash_list(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        return await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
    
    guilds = bot.guilds
    if guilds:
        response = 'I am in the following servers:\n'
        for guild in guilds:
            response += f'{guild.name} (ID: {guild.id})\n'
        await interaction.response.send_message(response)
    else:
        await interaction.response.send_message('I am not in any servers.')

@bot.tree.command(name="leave", description="Make the bot leave a server")
async def slash_leave(interaction: discord.Interaction, guild_id: int):
    if interaction.user.id != OWNER_ID:
        return await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
    
    guild = bot.get_guild(guild_id)
    if guild:
        await guild.leave()
        await interaction.response.send_message(f'Left the server: {guild.name}')
    else:
        await interaction.response.send_message('I am not in that server or invalid ID.')

def run_discord_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8000, 'debug': False})
    flask_thread.start()
    
    # Run the Discord bot in the main thread
    run_discord_bot()
