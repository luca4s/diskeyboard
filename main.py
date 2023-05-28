import discord, pyautogui, json, asyncio, os
with open("config.json", "r") as file:
    config = json.load(file)
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        channel = bot.get_channel(config["channelid"])
        embed = discord.Embed(color=0x00ff00, title="Keyboard online.", description=f"Allowed keys:\n```json\n{config['keylist']}\n```")
        await channel.send(embed=embed)
    except Exception as e:
        print(f"Error: {e}")
@bot.event
async def on_message(message):
    if message.channel.id != config["channelid"] or message.author == bot.user:
        return
    keys = message.content.lower().split(" ")
    if len(keys) == 1:
        if keys[0] in config["keylist"]:
            pyautogui.keyDown(keys[0])
            await asyncio.sleep(config["holdtime"])
            pyautogui.keyUp(keys[0])
            print(f"{message.author} pressed {keys[0]}")
        elif config["write"]:
            pyautogui.write(keys[0], interval=config["holdtime"])
            print(f"{message.author} wrote {keys[0]}")
    elif (len(keys) == 2 and keys[0] in list(config["combos"].keys()) and keys[1] in config["keylist"]) or(len(keys) == 3 and keys[0] in list(config["combos"].keys()) and keys[1] in list(config["combos"].keys()) and keys[2] in config["keylist"]):
        for key in keys:
            pyautogui.keyDown(key)
        await asyncio.sleep(config["holdtime"])
        for key in keys:
            pyautogui.keyUp(key)
        print(f"{message.author} pressed {' + '.join(keys)}")
bot.run(config["token"])