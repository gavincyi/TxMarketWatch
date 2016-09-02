from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from src.handler import handler
import sys

if __name__ == '__main__':
    api_token = ''
    source = ''
    
    for i in range(1, len(sys.argv)-1, 2):
        arg_item = sys.argv[i]
        arg_val = sys.argv[i+1]

        if arg_item == "-t":    
            api_token = arg_val
        elif arg_item == "-s":
            source = arg_val
    
    if source == 'GOOGLE':
        msg_handler = handler()
    elif source == 'YAHOO':
        msg_handler = handler(handler.Source.YAHOO)
    else:
        print("Invalid source %s" % source)
        exit(1)
    
    print("API token = %s" % api_token)
    updater = Updater(api_token)
    updater.dispatcher.add_handler(CommandHandler('quote', msg_handler.quote_handler))