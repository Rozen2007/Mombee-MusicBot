from discord.ext import commands


class MyMusicBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print('Bot is ready')
    
    async def on_message(self, message):
        await self.process_commands(message)
    

bot = MyMusicBot(command_prefix="?")
bot.load_extension('jishaku')
bot.load_extension('music')

bot.run('ODE2MjcwNTE0MTEyMjk5MDM5.YD4hKA.zSm93jZt9HlMzpZsErSrici00sM')

# java -jar Lavalink.jar 