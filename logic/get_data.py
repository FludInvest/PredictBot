from tinkoff.invest import Client, OrderType, OrderDirection, CandleInterval, InstrumentStatus, PositionsResponse


import aiohttp
import asyncio
import pandas
import aiomoex
import asyncio
import pandas

from config import *

from datetime import *


with Client(tokens['tinkoff']) as client:
    shares = pandas.DataFrame(
        client.instruments.shares(
            instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
        columns=['currency', 'lot', 'figi', 'ticker', 'buy_available_flag',
                 'for_qual_investor_flag', 'api_trade_available_flag'])



async def get_data_aiomoex(ticker):
    async with aiohttp.ClientSession() as session:
            frame = pandas.DataFrame(await aiomoex.get_board_candles(
                session = session,
                security = ticker,
                interval=7))
            
            return frame






    


