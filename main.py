from telethon import TelegramClient, events
import asyncio

client = TelegramClient("session", 2427294, "7bb64c0340f2e917dcaccf97dec6adb4")

client.start()


@client.on(events.NewMessage(chats=[155836063]))
async def replier(event):
	await event.forward_to("@Processing_meaallh")
	


client.run_until_disconnected()
