import discord, random, requests, json
from discord.ext import commands

class yomomma(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = "yomomma")
    async def yomomma (self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        response = requests.get("https://api.yomomma.info/")
        json_load = json.loads(response.text)
        ym = json_load["joke"]
        await ctx.send(f"{member.mention} {ym}")
    
def setup(client):
    client.add_cog(yomomma(client))