#!/usr/bin/env python

import telegram
import stockquote
import urllib2

class handler:
    class Source:
        GOOGLE = 0,
        YAHOO = 1
    
    def __init__(self, source=Source.GOOGLE):
        self.source=source
    
    def quote_handler(self, bot, update):
        quote_instmt = update.message.text
        ret = ""
        is_error = False
        
        try:
            if self.source == Source.GOOGLE:
                ret = stockquote.from_google(quote_instmt)
            else:
                ret = stockquote.from_yahoo(quote_instmt)
        except urllib2.HTTPError as e:
            is_error = True
            
        if not is_error:
            bot.sendMessage(update.message.chat_id,
                            text=ret.str())
        else:
            bot.sendMessage(update.message.chat_id,
                text="Invalid instrument: %s" % quote_instmt)
            