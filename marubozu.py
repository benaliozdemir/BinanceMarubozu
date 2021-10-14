import os

from binance.client import Client

from PIL import Image, ImageEnhance
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import telegram
from PIL import ImageFont
from PIL import ImageDraw 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import time
from dateutil import parser
import math
import os.path
import time
import plotly.graph_objects as go
from datetime import datetime
import mplfinance as mpf
import os
from datetime import date

start_time = time.time()




TELEGRAM_BOT_TOKEN = '2012524709:AAH9G21vDNTZyrGxTTbFpx2m-PwHBY_fmsU'
TELEGRAM_CHAT_ID = '-589824218'



binance_api_key = ''
binance_api_secret = ''

binsizes = { "4h": 60}
batch_size = 4

names=['BTCUSDT','ADAUSDT','AIONUSDT','ALGOUSDT','ALICEUSDT','ALPACAUSDT','ALPHAUSDT','ANKRUSDT','ARDRUSDT','ARUSDT','ATAUSDT','ATOMUSDT','AVAUSDT','AVAXUSDT','BTCUSDT','BANDUSDT','BATUSDT','BCHUSDT','BLZUSDT','BTTUSDT','BURGERUSDT','CHRUSDT','CHZUSDT','CKBUSDT','COCOSUSDT','COSUSDT','COTIUSDT','CRVUSDT','CTKUSDT','CTSIUSDT','CTXCUSDT','CVCUSDT','TCTUSDT','DASHUSDT','DATAUSDT','DCRUSDT','DEGOUSDT','DENTUSDT','DGBUSDT','DNTUSDT','DOGEUSDT','DOTUSDT','DREPUSDT','DUSKUSDT','EGLDUSDT','ENJUSDT','EOSUSDT','ETCUSDT','ELFUSDT','FETUSDT','FILUSDT','FIROUSDT','FLMUSDT','FLOWUSDT','FTMUSDT','FTTUSDT','GRTUSDT','GTOUSDT','GALAUSDT','HBARUSDT','HIVEUSDT' ,'HNTUSDT' , 'HOTUSDT' , 'ICPUSDT' , 'ICXUSDT' , 'IOSTUSDT' , 'IOTAUSDT' , 'IOTXUSDT' , 'IRISUSDT' , 'JUVUSDT' , 'KEEPUSDT' , 'KEYUSDT' , 'KLAYUSDT' , 'KMDUSDT' , 'KSMUSDT' , 'LINAUSDT' , 'LITUSDT' , 'LRCUSDT' , 'LSKUSDT' , 'LTCUSDT' , 'LTOUSDT' , 'LUNAUSDT', 'MANAUSDT' , 'MASKUSDT' , 'MATICUSDT','ZENUSDT' , 'XECUSDT' , 'XRPUSDT' , 'XTZUSDT' , 'XLMUSDT' , 'XVGUSDT' , 'ZECUSDT','ZENUSDT','ZRXUSDT','ZILUSDT', 'STORJUSDT' , 'STPTUSDT' , 'STRAXUSDT' , 'STXUSDT' , 'SYSUSDT' , 'SOLUSDT' , 'SFPUSDT' , 'SKLUSDT' , 'SLPUSDT' , 'SXPUSDT' , 'SCUSDT' , 'SNXUSDT' , 'TWTUSDT' , 'TRBUSDT' , 'TRXUSDT' , 'TFUELUSDT' , 'TKOUSDT' , 'TLMUSDT' , 'TCTUSDT' , 'TVKUSDT' , 'UTKUSDT' , 'UNFIUSDT' , 'VETUSDT' , 'VTHOUSDT' , 'VITEUSDT' , 'VIDTUSDT' , 'WRXUSDT' , 'WTCUSDT' , 'WINGUSDT' , 'WANUSDT' , 'WAVESUSDT' , 'WAXPUSDT','WNXMUSDT', 'MINAUSDT' , 'MITHUSDT' , 'MBOXUSDT' , 'NBSUSDT' , 'NEARUSDT' , 'NULSUSDT' , 'NKNUSDT' , 'OCEANUSDT' , 'OGNUSDT' , 'OMGUSDT' , 'OMUSDT' , 'ONEUSDT' , 'ONGUSDT' , 'ONTUSDT' , 'OXTUSDT' , 'PAXGUSDT' , 'PHAUSDT' , 'PNTUSDT' , 'POLSUSDT' , 'PONDUSDT' , 'PSGUSDT' , 'PUNDIXUSDT' , 'POLYUSDT' , 'PROMBUSD' , 'QNTUSDT' , 'QTUMUSDT' , 'QUICKUSDT' , 'RIFUSDT' , 'RLCUSDT' , 'ROSEUSDT' , 'RSRUSDT' , 'RVNUSDT' , 'SANDUSDT' , 'STMXUSDT','MBLUSDT' , 'MDTUSDT' ]


def main():

    for i in range(len(names)):
        print("Checking Bullish Marubozu on  ",names[i])
        bina = Client('','')
        klines = bina.get_historical_klines(names[i], Client.KLINE_INTERVAL_4HOUR,"1 day ago UTC",limit=4)
        data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
        data=data.apply(pd.to_numeric)
        data['ts'] = pd.to_datetime(data['ts'], unit='ms')
        df=data

        fig = go.Figure(data=[go.Candlestick(x=df.index,open=df['o'],high=df['h'],low=df['l'],close=df['c'])])
        fig.update_layout(title="<b>"+names[i]+"</b>", font=dict(
            family="Courier New, bold",
            size=50
        ))


        '''
        if Data[i, 3] > Data[i, 0] and Data[i, 1] == Data[i, 3] and Data[i, 2] == Data[i, 0]:
                    
                        Data[i, 6] = 1 
        '''

        print (data)



        for i in range(len(data)):
            if (data['c'][i] > data['o'][i] and data['h'][i] == data['c'][i] and data['l'][i] == data['o'][i]):
                print("MARUBOZU DETECTED ON ",names[i])
                bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="****From Binance MARUBOZU Bot*****")
                bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Marubozu detected on "+names[i])
                



while (1):
    main()
    print("Sleeping")
    time.sleep(14400)