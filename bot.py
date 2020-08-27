# requires python modules LXML, Yfinance, and python-telegram-bot 

import yfinance as yf
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_data():
    apple_data = yf.Ticker("AAPL")

    data = apple_data.info
    return data


def get_price():
    current_price = get_data()['bid']

    return f' The current price of AAPL is ${current_price}'


def get_summary():
    current_data = get_data()
    day_high, day_low, current_price = current_data['dayHigh'], current_data['dayLow'], current_data['bid']

    return f' Day Summary\nDay High: {day_high}\nDay Low: {day_low}\nCurrent Price: {current_price}'


def get_grout_worth():
    grout_worth = get_data()['bid'] * 60

    return f"Gunt's Apple shares are worth ${round(grout_worth)}"


def show_help():
    help_message = ("Help Menu\n"
                    "/price - will display the current price of AAPL\n"
                    "/worth - will display the total price of AAPL * 60\n"
                    "/summary - will display a basic summary of todays prices\n")

    return help_message


def price(update, context):
    """Sends current price of apple share when command /price is issued"""
    update.message.reply_text(get_price())


def worth(update, context):
    """Sends current apple share price * 60 when command /worth is issued"""
    update.message.reply_text(get_grout_worth())


def summary(update, context):
    """Sends the current summary for the day when the command /summary is issued"""
    update.message.reply_text(get_summary())


def help_command(update, context):
    """Displays help menu when command /help is issued"""
    update.message.reply_text(show_help())


def main():
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("worth", worth))
    dp.add_handler(CommandHandler("summary", summary))
    dp.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
