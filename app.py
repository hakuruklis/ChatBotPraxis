from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

praxis_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#praxis_bot.set_trainer(ChatterBotCorpusTrainer)
#praxis_bot.train("chatterbot.corpus.spanish")
#praxis_bot.train("chatterbot.corpus.praxis")



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(praxis_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
