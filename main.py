from pyrogram import Client

app = Client("session", 2427294, "7bb64c0340f2e917dcaccf97dec6adb4")


@app.on_message()
def my_handler(client, message):
    message.forward("me")


app.run()
