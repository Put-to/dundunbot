import discord, random, requests, json
from discord.ext import commands

class quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def quote(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        q = json_data[0]['q'] + ' -' + json_data[0]['a']
        await ctx.send(q)
    
def setup(client):
    client.add_cog(quotes(client))