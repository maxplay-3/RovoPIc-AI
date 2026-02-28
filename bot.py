import telebot
import main as RovoPicAI
TOKEN = "8355262126:AAExi-EFrxJ-jp4uQ7AY9moYXjCTrgeVElw"
bot = telebot.TeleBot(TOKEN)
ai = RovoPicAI.AI()


@bot.message_handler(commands=["start","help"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне фото")




@bot.message_handler(content_types=["photo"])
def handle_photos(message):
    userid = message.from_user.id
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"photo_{userid}.png", "wb") as f:
        f.write(downloaded_file)
    img = RovoPicAI.Image(f"photo_{userid}.png")
    result = ai.evaluate_image(img)
    if result == 0.3:
        result = f"{result}(плохо)"
        bot.reply_to(message, f"оценка(баллы): {result}")
    elif result == 3:
        result = f"{result}(отлично)"
        bot.reply_to(message, f"оценка(баллы): {result}")
    elif result == 1.2 or result == 1 or result == 1.3:
        result = f"{result}(не плохо)"
    bot.reply_to(message, f"оценка(баллы): {result}")
    
if __name__ == "__main__":
    bot.polling()