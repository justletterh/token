import discord,json
from sys import argv as args
t=args[1]
client=discord.Client()
dat={}
@client.event
async def on_ready():
    dat.update({"fullname":client.user,"token":t,"id":client.user.id,"discrim":client.user.discriminator,"name":client.user.name,"created at":client.user.created_at,"avatar":client.user.avatar_url})
    await client.close()
client.run(t)
for i in dat:
    dat[i]=str(dat[i])
print(json.dumps(dat))