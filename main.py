from bs4 import BeautifulSoup
import datetime
import requests
import json
import discord
import asyncio

client = discord.Client()
with open("links.json", "r") as f:
    links = json.load(f)


@client.event
async def on_ready():
    while True:
        channel = client.get_channel(here paste channel ID)
        req = requests.get('here paste link to raffle') #for example: https://www.soleretriever.com/raffles/nike-vaporwaffle-sacai-tan-navy-dd1875-200
        soup = BeautifulSoup(req.text, "html.parser")

        for a in soup.find_all("img", class_="zanrti-3 jxsqzH"):
            shoeName = a.get("alt")
            shoeImage = a.get("src")

            for img in soup.find_all("div", alt="Open raffle"):
                link = img.find("a", target="_blank").get("href")
                site = img.find("img").get("alt")
                image = img.find("img").get("src")
                ends = img.find("div", color="darkGray").text
                raffleType = img.find("div", class_="sc-bdvvaa sc-gsDJrp itMAzf jXLjZO").find_all("div")[0].text
                region = img.find("div", class_="sc-bdvvaa sc-gsDJrp itMAzf jXLjZO").find_all("div")[1].text
        
                if link not in links:
                    links.append(link)
                    embed = discord.Embed(title=shoeName, url=link, timestamp=datetime.datetime.utcnow(), color=0x5377e9)
                    embed.set_thumbnail(url=image)
                    embed.add_field(name="Ends:", value=ends)
                    embed.add_field(name="Site:", value=site, inline=False)
                    embed.add_field(name="Type:", value=raffleType, inline=False)
                    embed.add_field(name="Region:", value=region, inline=False)
                    embed.set_image(url=shoeImage)
                    embed.set_footer(text="Made by nullek#4646 | @nullek2")
                    msg = await channel.send(embed=embed)
                    await msg.add_reaction("✅")
                    with open("links.json","w") as f:
                        json.dump(links,f)

    await asyncio.sleep(60*10)

client.run("here paste your bot token")
