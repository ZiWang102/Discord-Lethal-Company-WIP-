from hashlib import new
import discord
import random
import os
import time
import bloobotviews
import bloobotmethods
from dotenv import load_dotenv
load_dotenv()
bloobot = discord.Bot()

started = False

@bloobot.event
async def on_ready() :
    print(f"Bloo is primed and ready")

@bloobot.slash_command(name = "hello", description = "Say hello to Bloo")
async def hello(ctx):
    embed = discord.Embed(
        title="Hello c:",
        color=discord.Colour.blurple()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/986250722205114401/996396783557161051/Bee_Happy_Emote.png")
    await ctx.respond("",embed=embed)

@bloobot.slash_command(name = "multiply", description = "Multiplies two numbers")
async def mult(ctx, number1, number2):
    sum = float(number1)*float(number2)
    await ctx.respond(f"Multiplication = {sum}")

@bloobot.slash_command(name = "divide", description = "Divides two numbers")
async def div(ctx, number1, number2):
    sum = float(number1)/float(number2)
    await ctx.respond(f"Division = {sum}")

@bloobot.slash_command(name = "company", description= "Hub of choices")
async def company(ctx):
    txt2 = "ALL THE STUFF PEOPLE CAN DO"
    embed = discord.Embed(
        title="DECISIONS",
        description=txt2,
        color=discord.Colour.blurple()
    )
    menu_view = bloobotviews.MenuView(ctx)
    await ctx.respond("",view=menu_view,embed=embed)
    
@bloobot.slash_command(name = "newgame", description = "Restart")
async def begin(ctx):
    view_var = bloobotviews.StartView(ctx)
    global started
    if started == False:
        started = True
        view_var = bloobotviews.StartView(ctx)
        txt1 = "ENTER START TEXT HERE (PROBABLY LETHAL COMPANY STUFF)"
        embed = discord.Embed(
            title="Beginning",
            description=txt1,
            color=discord.Colour.blurple()
        )
        await ctx.respond("", view=view_var,embed=embed)
    else:
        txt2 = "DO /company instead something something"
        embed = discord.Embed(
            title="Beginning",
            description=txt2,
            color=discord.Colour.blurple()
        )
        await ctx.respond("",embed=embed)

bloobot.run(os.getenv('TOKEN'))