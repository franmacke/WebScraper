from .TelegramBot import TelegramBot
from .Scrapper import WebScrapper
from dotenv import load_dotenv
import os
import time, datetime

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

class Application:
    def __init__(self) -> None:
        self.bot = TelegramBot(BOT_TOKEN)
        self.scrapper = WebScrapper()

    def run(self):
        self.scrapper.initWebDriver()
        estado = False

        while not estado:
            estado = self.scrapper.update()
            self.bot.update(estado)

            print(datetime.datetime.now())

            time.sleep(1)