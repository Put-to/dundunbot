import discord, os, json, sys
from discord.ext import commands
from discord.ext.commands.core import command

class mod(commands.Cog, name = "Moderation"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'kick', pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason = "Not Specified"):
        """kick a user out of the server"""
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title = "Error!",
                description = "User has admin parmissions.",
                color = 0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                await member.kick(reason = reason)
                embed = discord.Embed(
                    title = "User Kicked!",
                    description = f"**{member}** was kicked by **{context.message.author}**",
                    color = 0x42F56C
                )
                embed.add_field(
                    name = "Reason: ",
                    value = reason
                )
                await context.send(embed = embed)
                try:
                    await member.send(
                        f"You were Kicked by **{context.message.author}**! \n Reason: {reason}"
                    )
                except:
                    pass
            except:embed = discord.Embed(
                title="Error!",
                description= "An error occured while trying to Kick user. Make sure my role is above the role of the user to be kicked.",
                color = 0xE02B2B
            )
            await context.message.channel.send(embed = embed)
    
    @commands.command(name = "nick")
    @commands.has_permissions(manage_nicknames = True)
    async def nick(self, context, member:discord.Member, *, nickname = None):
        """Change the nickname of User"""
        try:
            await member.edit(nick = nickname)
            embed = discord.Embed(
                title = "Changed Nickname!",
                description = f"**{member}'s** new Nickname is  **{nickname}**!",
                color = 0x42f599
            )
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Error!",
                description = "An error occurred while changing the nickname. Make sure my role is above the role of the user you want to change the nickname.",
                color = 0xFF0000
            )
            await context.message.channel.send(embed = embed)


    @commands.command(name = "nickname")
    async def nickname(self, context, *, nickname = None):
        try:
            await context.message.author.edit(nick = nickname)
            embed = discord.Embed(
                description = f"**Changed Nickname to {nickname}**",
                color = 0x42f599
            )
            await context.send(embed = embed)
        except:
            embed = discord.Embed(
                title = "Error!",
                description = "An error occurred while changing the nickname. Make sure my role is above the role of the user you want to change the nickname.",
                color = 0xFF0000
            )
            await context.message.channel.send(embed = embed)

    
    @commands.command(name = "warn")
    @commands.has_permissions(manage_messages = True)
    async def warn(self, context, member : discord.Member, *, reason = "Not Specified"):
        embed = discord.Embed(
            title = "User Warned!",
            description = f"**{member}** was warned by **{context.message.author}**!",
            color = 0x42F56C
        )
        embed.add_field(
            name = "Reason: ",
            value = reason
        )

        try:
            await member.send(f"You were warned by **{context.message.author}**!\nReason: {reason}")
            await context.message.channel.send(embed = embed)
        except:
            pass

    @commands.command(name = "mute")
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, user:discord.Member):
        muted_role = discord.utils.find(lambda r: r.name.upper() == 'MUTED', ctx.guild.roles)
        if muted_role:
            if muted_role in user.roles:
                await ctx.send("That person is already muted!")
            else:
                await user.add_roles(muted_role)
                await ctx.send(f"**{user}** has been muted.")
        else:
            await ctx.send("Couldn't find a role with 'muted' in the name.")
    
    
    @commands.command(name = "unmute")
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.find(lambda r: r.name.upper() == 'MUTED', ctx.guild.roles)
        if muted_role:
            if muted_role in member.roles:
                await member.remove_roles(muted_role)
                await ctx.send(f"**{member}** has been unmuted.")
            else:
                await ctx.send("That person is not muted!")
        else:
            pass

    
   # @commands.group(name = "blacklist")
    #async def blacklist(self, context):

def setup(bot):
        bot.add_cog(mod(bot))