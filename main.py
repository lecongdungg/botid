import telebot
from keep_alive import keep_alive  # Import hàm keep_alive
# Thay thế 'YOUR_BOT_TOKEN' bằng token của bot bạn đã tạo từ @BotFather trên Telegram
bot = telebot.TeleBot('7271455827:AAFi-Gq_34Va8Gu00aXds-bKyVnaVarLi48')
keep_alive()  # Khởi động server Flask để giữ cho bot hoạt động liên tục

@bot.message_handler(commands=['start'])
def send_welcome(message):
  user_id = message.from_user.id
  user_name = message.from_user.first_name
  bot.reply_to(
      message,
      f"Chào {user_name} (ID: {user_id})!\nTôi là Bot Check ID người dùng và nhóm.\n"
      f"Để kiểm tra ID của bạn, hãy sử dụng lệnh\n/id.\n"
      f"Để kiểm tra ID của nhóm, hãy sử dụng lệnh\n/nhom.")


@bot.message_handler(commands=['id'])
def send_user_id(message):
  user_id = message.from_user.id
  bot.reply_to(message, f"ID của bạn là : {user_id}")


@bot.message_handler(commands=['nhom'])
def send_group_id(message):
  chat_id = message.chat.id
  bot.reply_to(message, f"ID của nhóm là : {chat_id}")


# Không quên chạy bot với mã sau:
bot.polling()
