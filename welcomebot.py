#!/usr/bin/env python3
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
idchannel = 740777672220606555

greeting = """
Welcome to the Peppercon Discord Server
We welcome and encourage participation from members with varied backgrounds and experiences.
Inclusivity and diversity are part of what make Peppercon interesting and valuable.
It is our goal to create a welcoming and safe space for everyone.
The only pain and misery caused by Peppercon should be the beautiful pain of our spice.

Expected Behavior:
Be welcoming
Be kind
Be respectful
Look out for each other

Unacceptable Behavior
Violence, threats of violence or violent language directed against another person.
Sexist, racist, homophobic, transphobic, ableist or otherwise discriminatory jokes and language.
Posting or threatening to post other people’s personally identifying information (“doxing”).
Personal insults, particularly those related to gender, sexual orientation, race, ethnicity, religion, or disability.
Inappropriate photography or recording.
Unwelcome sexual attention. This includes sexualised comments or jokes, and unwelcome sexual advances.
Deliberate intimidation, stalking or following.
Advocating for, or encouraging, any of the above behaviour.
This list is non-exhaustive. Keep in mind the expected behaviors when deciding if something you want to say or do is appropriate.

Conflict Resolution
If you see someone violating the code of conduct, you are encouraged to address the behavior directly with those involved.
Many issues can be resolved quickly and easily, and this gives people more control over the outcome of their dispute.
If you are unable to resolve the matter for any reason, or if the behavior is threatening or harassing,
report it to a Founder (identified in Discord by a name highlighted in BLUE or BLACK).
The Founder will investigate and if a violation occurred, the Founders will use our discretion in determining when and how to follow up on the incident,
which may range from not taking action to permanent expulsion
"""

@client.event
async def on_ready():
        print(f'Peppercon Welcome Bot ready to greet!')

@client.event
async def on_member_join(member):
        try:
                await member.send(greeting)
        except:
                print("There was an error sending the terms")
        await client.get_channel(idchannel).send(file=discord.File(r'/home/blakhal0/Desktop/images/welcome.gif'))

client.run('SECRET_KEY_HERE')
