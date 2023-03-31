from discord.ext import commands
import hmtai

class Hentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def classic(self, ctx):
        await ctx.send(hmtai.get("hmtai", "classic"))

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def anal(self, ctx):
        await ctx.send(hmtai.get("hmtai", "anal"))

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def ass(self, ctx):
        await ctx.send(hmtai.get("hmtai", "ass"))

    @commands.is_nsfw()
    @commands.command(pass_context=True)
    async def masturbation(self, ctx):
        await ctx.send(hmtai.get("hmtai", "masturbation"))

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def public(self, ctx):
        await ctx.send(hmtai.get("hmtai", "public"))

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def bdsm(self, ctx):
        await ctx.send(hmtai.get("hmtai", "bdsm"))

async def setup(bot):
    await bot.add_cog(Hentai(bot))