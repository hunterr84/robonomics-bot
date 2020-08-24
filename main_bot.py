import telebot
import query
import os


API_TOKEN = os.getenv('TOKEN_ROBONOMICS')
bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    inline_btn_1 = telebot.types.InlineKeyboardButton('Robonomics', callback_data='substrate_robonomics')
    inline_btn_2 = telebot.types.InlineKeyboardButton('DAO IPCI', callback_data='substrate_dao')
    keyboard.add(inline_btn_1, inline_btn_2)
    bot.send_message(message.chat.id,
        "Welcome! \n\n"
        "Robonomics Network is a set of open-source packages for Robotics, Smart Cities and Industry 4.0 developers.\n\n"
        "Select network to check status:\n", reply_markup=keyboard)


@bot.callback_query_handler(lambda callback_query: True)
def process_callback_button(callback_query: telebot.types.CallbackQuery):
    keyboard = telebot.types.InlineKeyboardMarkup()
    answer_data = callback_query.data
    git_button = telebot.types.InlineKeyboardButton(text="GitHub", url="https://github.com/airalab/robonomics/releases")
    parachain_button = telebot.types.InlineKeyboardButton(text="Explorer", url="https://parachain.robonomics.network")
    keyboard.add(git_button, parachain_button)
    parachain_name, version, token, peers_count, block_hash, block_number, block_timestate = query.get_network_status(
        answer_data)
    bot.send_message(callback_query.from_user.id, f"Name: {parachain_name}\n"
                                                  f"Version: {version}\n"
                                                  f"Token: {token}\n"
                                                  f"Peers: {peers_count}\n"
                                                  f"Last block: {block_number}\n"
                                                  f"Block timestate: {block_timestate}\n"
                                                  f"Block hash: {block_hash}", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)