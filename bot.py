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
    return "Welcome to DevsCertificated"

DISCORD_TOKEN = os.getenv('token')

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

def run_discord_bot():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'debug': False})
    flask_thread.start()
    
    # Run the Discord bot in the main thread
    run_discord_bot()
