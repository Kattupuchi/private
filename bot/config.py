import os

class Config:
    TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
    SUDOS=os.environ['SUDOS', "5599715194"]
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH', "8da8adb41f654ba374788eb88003c3c4"]
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID', "9531120"])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
