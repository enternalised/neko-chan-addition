from discord.ext.commands import Bot
import random

TOKEN = 'Token'
bot = Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("Login as")
    print(bot.user.name)
    print("-------")

@bot.command(name='8ball')
async def magic_eight_ball(ctx):
    response =[
        'Without a doubt.', 
        'Outlook good.', 
        'Better not tell you now.', 
        'Cannot predict now.',
        'My reply is no.', 
        'Outlook not so good.',
    ]

    await ctx.send(random.choice(response))

bot.run(TOKEN)
