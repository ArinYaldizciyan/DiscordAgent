from discord_typings import MessageCreateEvent
from interactions import Client, Intents, listen, slash_command, SlashContext, Message
from main import translate
import os
import re

bot = Client(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print(bot.user.id)
    print(bot.user.tag)
    print(bot.user)
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen()
async def on_message_create(event: MessageCreateEvent):
    msg: Message = event.message
    message_content = msg.content
    stripped_content = re.sub(r'<[^>]*>', '', message_content)
    # Get all mentioned users in the message
    async for user in msg.mention_users:
        if user.id == bot.user.id:
            if not stripped_content:
                await msg.reply("Please provide text to translate.")
            else:
                response = translate(stripped_content, "Japanese")
                await msg.reply(response.content[:2000])
            break

bot.start(os.environ.get("DISCORD_BOT_KEY"))