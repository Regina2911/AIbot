# Cat Breed Classifier Bot 🐱

A Telegram bot that can identify cat breeds from user-submitted photos.

## What it does

- You send a photo of a cat to the bot
- The bot uses a trained machine learning model
- It tells you what breed the cat is

## How to use

Just send a picture of a cat to the bot in Telegram, and it will respond with the predicted breed.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/cat-breed-classifier-bot.git
cd cat-breed-classifier-bot

2. Install requirements:
pip install -r requirements.txt

3. Set your Telegram token in `.env` file:
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

4. Run the bot:
python bot.py

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
