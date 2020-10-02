# TxMarketWatch
Telegram bot - Market data provider.

This is amazing projects for beginners.

## Prerequisite 

Please create the bot in [BotFather](https://telegram.me/BotFather) first. 
For details please refer to https://core.telegram.org/bots.

## Installation

Install packages through pip

```
pip install -r requirements.txt
```

Start the bot in python

```
python TxMarketWatch -t <token> -s <source>
```

The supported argument(s) 

|Argument|Description|
|:---:|:---:|
| -t | Telegram bot token |
| -s | Quote source, either "GOOGLE" or "YAHOO" |


## Command

User can send command */quote* for stock quote. For example, 

```
/quote NASDAQ:GOOG
```

returns the quote of instrument *NASDAQ:GOOG*.

## Acknowledgment

Thanks to github user mdengler for providing a slim stock quote python script.

The [script](https://github.com/mdengler/stockquote.git) is under src/stockquote.py.




