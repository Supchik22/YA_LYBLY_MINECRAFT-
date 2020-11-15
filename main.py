import asyncio # needed for sleep that won't block the bot, only for this example
import discord
from discord.ext import commands
import PIL
from discord.utils import get




#NzY3NjM1NzgwNTk5MjgzNzIy.X40yiA.JuZn6Yq1-Akn4ad9SbascPcz_-M

TOKEN = "NzY4NzA5MDU0NTAzMDU5NDU2.X5EaGA.gAjUdD1eUMRy5oVhwm5aEVolhxE"
bot = commands.Bot(command_prefix='(')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('бот в сети! ураааа')
    activity = discord.Game(name="MEOW", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    while True:
        await asyncio.sleep(5)
        activity = discord.Game(name=f"Servers: {len(bot.guilds)}", type=2)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        activity = discord.Game(name="(help", type=2)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(5)
        
        await bot.change_presence(activity=discord.Streaming(name="Discord", url='https://www.twitch.tv/supchik090'))



@bot.command()
async def help(ctx , arg=None):
    if arg == None:
      await ctx.send('💎(help Moder - Moderation \n (help Basic - Basic commands💎')
    
    if arg == 'Moder':
      embed = discord.Embed(title="help",description="💎 Moderator Commands💎\n  (clearchat cls  - clear chat \n (kick @user \n ")
      embed.add_field(name="By supchik", value="Discord.Py", inline=True)
      await ctx.send(embed=embed)
    if arg == 'Basic':
      embed = discord.Embed(title="help",description="💎 Basic Commands💎\n  (help  - help commands \n (tree - Pixel art tree \n (grassblock - Pixel art grassblock ")
      embed.add_field(name="By supchik", value="Discord.Py", inline=True)
      await ctx.send(embed=embed)


#@bot.event
#async def on_message(message):
#  await bot.process_commands( message )





@bot.command(name='нет_да')
async def no_yes(ctx ,no ,yes):
  
  gg = Image.open("yes_no.png")



  idraw = ImageDraw.Draw(gg)
  text = "TEXT"

  font = ImageFont.truetype("arial.ttf", size=18)

  idraw.text((10, 10), text, font=font)

  gg.save('No_hol.png')

  file = discord.File("No_hol.png", filename="No_hol.png")
  await ctx.channel.send("No yes", file=file)
  


@bot.command()
@commands.has_permissions(administrator=True) #administrator=True
async def clearchat(ctx, cls=100):
    await ctx.channel.purge(limit=cls)
    print("команда Clear Успешно выполнена")


    #    f = open(f'coin\{user.id}\coin.score', 'r')
    #    coins = f.read()
    #    embed = discord.Embed(title="BANK", description=f"{user} score is :{coins}", color=0x36b125)
    #    embed.set_thumbnail(
    #        url="https://media.discordapp.net/attachments/552851579552792578/770222658699788308/Coin.png")
    #    embed.add_field(name="Marokki Coin", value="Balance", inline=True)
    #    await ctx.send(embed=embed)
    #    f.close()







@bot.command() # просто для бота
async def grassblock(ctx): # Команда
    await ctx.send("Grass_block \n🟩🟩🟩🟩🟩\n🟩🟫🟩🟫🟩\n🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫")
    await ctx.message.add_reaction("✅")




@bot.command() # просто для бота
async def tree(ctx): # Команда
    await ctx.send("Tree \n🟦🟦🟩🟨\n🟦🟩🟩🟩\n🟦🟦🟫🟦\n🟦🟦🟫🟦\n🟩🟩🟩🟩")
    await ctx.message.add_reaction("✅")



@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member ,* ,prichin):
    pikachu = '<:Pickachu:770176119247994881>'
    await user.kick(reason=prichin)
    await ctx.send(f"{pikachu} R.I.P {pikachu}")
    if user == None:
          await ctx.send(f"{pikachu} NOT user {pikachu}")
      



bot.run('NzY4NzA5MDU0NTAzMDU5NDU2.X5EaGA.gAjUdD1eUMRy5oVhwm5aEVolhxE')



