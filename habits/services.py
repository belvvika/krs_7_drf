import request
from config.settings import TG_BOT_ID

def send_message(message, chat_id):
    params = {'chat_id': chat_id, 'text': message}
    request.get(f"https://api.telegram.org/bot{TG_BOT_ID}/sendMessage", params=params)
