import discord, requests
from discord.ext import commands
import translators as ts

class translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = "translate")
    async def translate (self, ctx, *, trans):
        embed = discord.Embed(title = f'Request by{ctx.author}', description =trans, )
        try:
            embed.add_field(
                name = "Translation: ",
                value = ts.google(trans)
            )
        except Exception as e:
            embed.add_field(
                name = "Error",
                value=e
            )
        
        await ctx.send(embed = embed)
    
def setup(client):
    client.add_cog(translate(client))