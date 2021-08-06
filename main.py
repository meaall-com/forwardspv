from pyrogram import Client

app = Client("myssion", 2427294, "7bb64c0340f2e917dcaccf97dec6adb4")


@app.on_message()
def my_handler(client, message):
    print(message)
    message.forward("me")


app.run()
