import discord, random, requests, json
from discord.ext import commands

class gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = "gif")
    async def gif(self, ctx, *, search = None):

      #  await ctx.message.add_reaction('<:easygif_roger:712005159676411914>')
        embed = discord.Embed(title='From {}'.format(ctx.author),description = f"Command issued: gif {search}", colour=discord.Colour.blue())

        if not search:  
            random_search_key = ['anime', 'manga', 'japan', 'japanese+animation', 'menhera', 'cute+anime', 'cat', 'dog', 'meme', 'anime+funny']
            choosing_from_random_search_key = random.randint(0,len(random_search_key) - 1)
            random_search_term = random_search_key[choosing_from_random_search_key]
            response = requests.get('https://api.tenor.com/v1/search?q=' + random_search_term + '&key=' + '0VKZAG5EU21U' + '&limit=50')
            data = json.loads(response.text)
            gif_choice = random.randint(0, 49)
            result_gif = data['results'][gif_choice]['media'][0]['gif']['url']

            embed.set_image(url=result_gif)
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/tenor/tenor-logo.png", text="Powered by Tenor")

            await ctx.send(embed=embed)
            await ctx.message.delete()

               

        else:


            search.replace(' ', '+')

            response = requests.get('https://api.tenor.com/v1/search?q=' + search + '&key=' + "0VKZAG5EU21U" + '&limit=3')
            data = json.loads(response.text)

            gif_choice = random.randint(0, 2)
            result_gif = data['results'][gif_choice]['media'][0]['gif']['url']

            embed.set_image(url=result_gif)
            embed.set_footer(icon_url="https://easygif-assets.netlify.app/assets/public/logos/tenor/tenor-logo.png", text="Powered by Tenor")

            await ctx.send(embed=embed)
            await ctx.message.delete()

    
def setup(client):
    client.add_cog(gif(client))