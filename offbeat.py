import discord
from discord.ext import commands



client = commands.Bot(command_prefix=">")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="No reason provided"):
  try:
    await member.kick(reason=reason)
    await member.send("You have been kicked from the Offbeat's Realm because of {}".format(reason))
    em = discord.Embed(title=f"{member} is kicked.")
    await ctx.send(embed=em)
  except Exception as e:
    await ctx.send(f"Error: {e}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="No reason provided"):
  try:
    await member.send("You have been banned from the OffBeat's Realm because of {}".format(reason))
    await member.ban(reason=reason)
    em = discord.Embed(title=f"{member} is banned for {reason}")
    await ctx.send(embed=em)
  except Exception as e:
    await ctx.send(f"Error: {e}")

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')


  for ban_entry in banned_users:
    user = ban_entry.user


    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return

@client.command()
async def warn(ctx, member : discord.Member, *, reason="No reason provided"):
  try:
    await member.send("You have been warned from the OffBeat's Realm because of {}".format(reason))
    em = discord.Embed(title=f"{member} is warned for {reason}")
    await ctx.send(embed=em)
  except Exception as e:
    await ctx.send(f"Error: {e}")

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
  muted_role = ctx.guild.get_role(799071192563580948)
  await member.add_roles(muted_role)
  await ctx.send(f"{member.display_name} is muted!")



@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
  muted_role = ctx.guild.get_role(799071192563580948)
  await member.remove_roles(muted_role)
  await ctx.send(f"{member.display_name} is unmuted!")


client.run("NzkyMTc0ODEyODA1NDY0MDY0.X-Z4SQ.9LhrTOnpo8Qe5r_1Vn9oDqX4irQ")



