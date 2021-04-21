from bs4 import BeautifulSoup
import datetime
import requests
import json
import discord
import asyncio

client = discord.Client()
with open("links.json","r") as f:
    links = json.load(f)

@client.event
async def on_ready():
  while True:
    channel = client.get_channel(834457864038252544)
    req = requests.get('https://www.soleretriever.com/raffles/nike-vaporwaffle-sacai-tan-navy-dd1875-200')
    soup = BeautifulSoup(req.text, "html.parser")

    for main in soup.find_all("div", class_="sc-bdfBwQ sc-gsTCUz zanrti-0 jzXtZT bhdLno cYEQVO"):
        shoeName = main.find("h1", color="text").text
        shoeImage = main.find("img").get("src")

        for img in soup.find_all("div", alt="Open raffle"):
            link = img.find("a", target="_blank").get("href")
            site = img.find("img").get("alt")
            image = img.find("img").get("src")
            ends = img.find("div", color="darkGray").text
            raffleType = img.find("div", class_="sc-bdfBwQ sc-gsTCUz jzXtZT bhdLno").find_all("div")[0].text
            region = img.find("div", class_="sc-bdfBwQ sc-gsTCUz jzXtZT bhdLno").find_all("div")[1].text
            if link not in links:
                links.append(link)
                embed = discord.Embed(title=shoeName , url=link , timestamp=datetime.datetime.utcnow(), color=0x5377e9)
                embed.set_thumbnail(url=image)
                embed.add_field(name="Ends:", value=ends)
                embed.add_field(name="Site:", value=site, inline=False)
                embed.add_field(name="Type:", value=raffleType, inline=False)
                embed.add_field(name="Region:", value=region, inline=False)
                embed.set_image(url=shoeImage)
                embed.set_footer(text="Doggify Monitors", icon_url="https://media.discordapp.net/attachments/808292830988599296/813544846496628776/test2.png")
                msg = await channel.send(embed=embed)
                await msg.add_reaction("✅")
                with open("ok.json","w") as f:
                    json.dump(ok,f)   

    await asyncio.sleep(60*5)

client.run("ODM0NDU4Nzk0NjU3NTc5MDE4.YIBMUA.D6f3oZaAiqRyCGg3r-VWsMWshmI")