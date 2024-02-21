import discord
import random
import os
import time
import bloobotmethods
import bloobotclasses

moons = bloobotmethods.init_moons()
catalogue = bloobotmethods.init_store()
current_moon = bloobotmethods.lookupdex("41-Experimentation",moons)
balance = 60
inventory = bloobotclasses.Inventory()

class StartView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(label="Ready", style=discord.ButtonStyle.blurple, emoji="✅")
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING READY",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="Quit", style=discord.ButtonStyle.blurple, emoji="❌")
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class MenuView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(label="Moons", style=discord.ButtonStyle.blurple, emoji="🌕")
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING READY",
        color=discord.Colour.blurple()
        )
        moon_view = MoonView(self.ctx)
        await self.ctx.respond("",view=moon_view,embed=embed)

    @discord.ui.button(label="Store", style=discord.ButtonStyle.blurple, emoji="🏬")
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        store_view = StoreView(self.ctx)
        await self.ctx.respond("",view=store_view,embed=embed)
    
    @discord.ui.button(label="Storage", style=discord.ButtonStyle.blurple, emoji="📦")
    async def button_callback3(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="Launch", style=discord.ButtonStyle.blurple, emoji="🚀")
    async def button_callback4(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)


    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class MoonView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(label="71-Gordion", style=discord.ButtonStyle.blurple,row=1)
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("71-Gordion",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)

    @discord.ui.button(label="41-Experimentation", style=discord.ButtonStyle.blurple, emoji="🇧", row=2)
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("41-Experimentation",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="220-Assurance", style=discord.ButtonStyle.blurple, emoji="🇩", row=2)
    async def button_callback3(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("220-Assurance",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="56-Vow", style=discord.ButtonStyle.blurple, emoji="🇨",row=2)
    async def button_callback4(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("56-Vow",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="21-Offense", style=discord.ButtonStyle.blurple, emoji="🇧",row=3)
    async def button_callback5(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("21-Offense",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="61-March", style=discord.ButtonStyle.blurple, emoji="🇧",row=3)
    async def button_callback6(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("61-March",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,0,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="85-Rend", style=discord.ButtonStyle.blurple, emoji="🇦",row=4)
    async def button_callback7(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("85-Rend",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,550,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="7-Dine", style=discord.ButtonStyle.blurple, emoji="🇸",row=4)
    async def button_callback8(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("7-Dine",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,600,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)
    
    @discord.ui.button(label="8-Titan", style=discord.ButtonStyle.blurple, emoji="🇸",row=4)
    async def button_callback9(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        selected_moon = bloobotmethods.lookupdex("8-Titan",moons)
        embed = discord.Embed(
        description=f"The cost to route to {selected_moon.fullname} is {selected_moon.cost}. It is currently {selected_moon.weather} on this moon. Please Confirm or Deny.",
        color=discord.Colour.blurple()
        )
        confirm_view = ConfirmMoonView(self.ctx,700,selected_moon)
        await self.ctx.respond("",view=confirm_view,embed=embed)

    @discord.ui.button(label="Info", style=discord.ButtonStyle.blurple,row=1)
    async def button_callback10(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="INFO STUFF",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Back", style=discord.ButtonStyle.blurple,row=1)
    async def button_callback11(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        back_view = MenuView(self.ctx)
        await self.ctx.respond("",view=back_view)


    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class StoreView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(label="Walkie-talkie", style=discord.ButtonStyle.blurple, emoji="🎙",row=1)
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOUND THAT HAPPENS THAT MAKES IT SEEM LIKE SOMETHING CHANGED",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="Flashlight", style=discord.ButtonStyle.blurple, emoji="🔦",row=1)
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Shovel", style=discord.ButtonStyle.blurple, emoji="🥄",row=1)
    async def button_callback3(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Lockpicker", style=discord.ButtonStyle.blurple, emoji="🔏",row=1)
    async def button_callback4(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Pro-flashlight", style=discord.ButtonStyle.blurple, emoji="🔦",row=2)
    async def button_callback5(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Stun grenade", style=discord.ButtonStyle.blurple, emoji="💥",row=2)
    async def button_callback6(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Boombox", style=discord.ButtonStyle.blurple, emoji="📻",row=2)
    async def button_callback7(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="TZP-Inhalant", style=discord.ButtonStyle.blurple, emoji="🫁",row=2)
    async def button_callback8(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Zap gun", style=discord.ButtonStyle.blurple, emoji="⚡",row=3)
    async def button_callback9(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Jetpack", style=discord.ButtonStyle.blurple, emoji="🚀",row=3)
    async def button_callback10(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Extension ladder", style=discord.ButtonStyle.blurple, emoji="🪜",row=3)
    async def button_callback11(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Radar-booster", style=discord.ButtonStyle.blurple, emoji="📡",row=3)
    async def button_callback12(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Back", style=discord.ButtonStyle.blurple,row=4)
    async def button_callback13(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        back_view = MenuView(self.ctx)
        await self.ctx.respond("",view=back_view)

    @discord.ui.button(label="NEXT PAGE",style=discord.ButtonStyle.blurple,row=4)
    async def button_callback14(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        store2_view = Store2View(self.ctx)
        await self.ctx.respond("",view=store2_view,embed=embed)
    
    @discord.ui.button(label="INFO", style=discord.ButtonStyle.blurple,row=4)
    async def button_callback15(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class Store2View(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()

    @discord.ui.button(label="Loud horn", style=discord.ButtonStyle.blurple, emoji="📢",row=1)
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOUND THAT HAPPENS THAT MAKES IT SEEM LIKE SOMETHING CHANGED",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="Signal Translator", style=discord.ButtonStyle.blurple, emoji="📺",row=1)
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Teleporter", style=discord.ButtonStyle.blurple, emoji="➡️",row=1)
    async def button_callback3(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Inverse Teleporter", style=discord.ButtonStyle.blurple, emoji="⬅️",row=1)
    async def button_callback4(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Green suit", style=discord.ButtonStyle.blurple, emoji="🟢",row=2)
    async def button_callback5(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Hazard suit", style=discord.ButtonStyle.blurple, emoji="☣️",row=2)
    async def button_callback6(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Pajama suit", style=discord.ButtonStyle.blurple, emoji="🎀",row=2)
    async def button_callback7(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="PREVIOUS PAGE", style=discord.ButtonStyle.blurple,row=3)
    async def button_callback8(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        prev_view = StoreView(self.ctx)
        await self.ctx.respond("",view=prev_view)

    @discord.ui.button(label="NEXT PAGE", style=discord.ButtonStyle.blurple,row=3)
    async def button_callback9(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        next_view = Store3View(self.ctx)
        await self.ctx.respond("",view=next_view)
    
    @discord.ui.button(label="INFO", style=discord.ButtonStyle.blurple,row=3)
    async def button_callback10(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)


    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class Store3View(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
    
    @discord.ui.button(label="PREVIOUS PAGE", style=discord.ButtonStyle.blurple,row=4)
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        prev_view = Store2View(self.ctx)
        await self.ctx.respond("",view=prev_view)

    @discord.ui.button(label="INFO", style=discord.ButtonStyle.blurple,row=4)
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="Cozy Lights", emoji='🌟',style=discord.ButtonStyle.blurple,row=1)
    async def button_callback3(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Goldfish", emoji='🐠',style=discord.ButtonStyle.blurple,row=1)
    async def button_callback4(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Jack O' Lantern", emoji='🎃',style=discord.ButtonStyle.blurple,row=1)
    async def button_callback5(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Television", emoji='📺',style=discord.ButtonStyle.blurple,row=1)
    async def button_callback6(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Record Player", emoji='🔉',style=discord.ButtonStyle.blurple,row=2)
    async def button_callback7(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Romantic Table", emoji='🟪',style=discord.ButtonStyle.blurple,row=2)
    async def button_callback8(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Shower", emoji='🚿',style=discord.ButtonStyle.blurple,row=2)
    async def button_callback9(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Table", emoji='🟫',style=discord.ButtonStyle.blurple,row=2)
    async def button_callback10(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Toilet", emoji='🚽',style=discord.ButtonStyle.blurple,row=3)
    async def button_callback11(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Welcome Mat", emoji='🔲',style=discord.ButtonStyle.blurple,row=3)
    async def button_callback12(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    
    @discord.ui.button(label="Plushie Pajama Man", emoji='🧸',style=discord.ButtonStyle.blurple,row=3)
    async def button_callback13(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)
    

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class ConfirmMoonView(discord.ui.View):
    def __init__(self, ctx, cost, moon):
        self.ctx = ctx
        self.cost = cost
        self.moon = moon
        super().__init__()

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.blurple, emoji="✅")
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        global balance
        global current_moon
        embed = discord.Embed(color=discord.Colour.blurple())
        if self.cost <= balance:
            balance -= self.cost
            embed.description = "SOMETHING SOMETHING HAPPENDED"
        else: 
            embed.description = "SOMETHING SOMETHING DID NOT HAPPEN BECAUSE UR BROOOOKE"
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="DENY", style=discord.ButtonStyle.blurple, emoji="❌")
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True

class ConfirmStoreView(discord.ui.View):
    def __init__(self, ctx, cost, item):
        self.ctx = ctx
        self.cost = cost
        self.item = item
        super().__init__()

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.blurple, emoji="✅")
    async def button_callback1(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        global balance
        global current_moon
        embed = discord.Embed(color=discord.Colour.blurple())
        if self.cost <= balance:
            balance -= self.cost
            embed.description = f"Ordered 1 {self.item.fullname}. Your new balance is {balance}.\nOur contractors enjoy fast, free shipping while on the job!"
        else: 
            embed.description = "SOMETHING SOMETHING DID NOT HAPPEN BECAUSE UR BROOOOKE"
        await self.ctx.respond("",embed=embed)

    @discord.ui.button(label="DENY", style=discord.ButtonStyle.blurple, emoji="❌")
    async def button_callback2(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(
        description="SOMETHING SOMETHING NOT READY (Do /newgame again if you change your mind)",
        color=discord.Colour.blurple()
        )
        await self.ctx.respond("",embed=embed)

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You are not allowed to interact with this",ephemeral=1)
            return False
        else:
            return True
