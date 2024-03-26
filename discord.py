
from disnake.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import disnake

from logic.predict_sklearn import *
from logic.get_data import *
from config import *
import asyncio



bot = commands.Bot()

@bot.slash_command()
async def prediction(iteration,ticker: str):
    webhook = DiscordWebhook(url=tokens['webhook'])

    if ticker.upper() in shares['ticker'].values:
        sk_predict = await predict(ticker)

        if sk_predict == "STRONG BUY":
            embed =  DiscordEmbed(title="Predict",color = "ADFF2F")
            embed.set_image(url = "https://bullvestorbb.com/wp-content/uploads/2023/08/INNO-Strong-buy.jpg")
            embed.add_embed_field(name = ' ' , value = "STRONG BUY")
        else:
            if sk_predict == "BUY":
                embed =  DiscordEmbed(title="Predict",color = "ADFF2F")
                embed.set_image(url = "https://www.meme-arsenal.com/memes/2c4b63c9e15048062e751a69fa6183fb.jpg")
                embed.add_embed_field(name = ' ' , value = "BUY")
            else:
                embed =  DiscordEmbed(title="Predict",color = "F0E68C")
                embed.set_image(url = "https://yt3.googleusercontent.com/ytc/AIdro_mB6km3CDNyP3sOvWkI1JO-1ZDbJjt7ePQFtRRI=s900-c-k-c0x00ffffff-no-rj")
                embed.add_embed_field(name = ' ' , value = "DONT BUY")

        
    else:
        embed =  DiscordEmbed(title="Predict",color = "8B0000")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj7Ip3tWiQEUCdhIl5IdetKOBOeOsNQtb1tw&usqp=CAU")
        embed.add_embed_field(name = " " , value= "Not Found Ticker")

    webhook.add_embed(embed)
    resourse = webhook.execute()

if __name__ == "__main__":
    bot.run(tokens['discord'])

