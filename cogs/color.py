import os
import sys
import time
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.utils import find
from discord.utils import get
import asyncio
import json
import random

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.red = 0xff0000
        self.orange = 0xff6600
        self.yellow = 0xfff200
        self.green = 0x00ff1a
        self.cyan = 0x00eeff
        self.blue = 0x000dff
        self.violet = 0x4c00ff
        self.pink = 0xff00ee
    
    @commands.command()
    @has_role("rainbow")
    async def rainbow(self, ctx, *,args=None):
        if (args == None):
            colors = [
                self.red,
                self.orange,
                self.yellow,
                self.green,
                self.cyan,
                self.blue,
                self.violet,
                self.pink
            ]
            random_color = random.choice(colors)
            with open("/config.json", "r") as f:
                data = json.load(f)
            role_name = data['Role_Name']
            rainbow_role = discord.utils.get(ctx.guild.roles, name=str(role_name))
            await rainbow_role.edit(colour=random_color)
            await ctx.message.delete()
            msg = await ctx.send("Your rainbow role color has been updated")
            await asyncio.sleep(7)
            await msg.delete()
        else:
            hex_1 = int(args, 16)
            hex_color = hex(hex_1)
            with open("/config.json", "r") as f:
                data = json.load(f)
            role_name = data['Role_Name']
            rainbow_role = discord.utils.get(ctx.guild.roles, name=str(role_name))
            await rainbow_role.edit(colour=hex_color)
            await ctx.message.delete()
            await ctx.send("Your rainbow role color has been updated")
            await asyncio.sleep(7)
            await msg.delete()

    @commands.command()
    async def about(self, ctx):
        author = ctx.message.author.name
        print(f"{author} Entered About Command")
        twilight_console_log = client.get_channel(665553350355582986)
        await twilight_console_log.send(f"**{author}** Entered **About** Command")
        embed=discord.Embed(title="JinnoB", description="Developed By: <@255876083918831616>", color=0x1cff93)
        embed.add_field(name="Website: ", value="https://powerthecoder.xyz", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))