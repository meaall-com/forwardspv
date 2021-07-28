from telethon import TelegramClient, events
import asyncio

client = TelegramClient("session", 1497933, "c0780c2359c081e206bbb180f3050a5c")

client.start()


@client.on(events.NewMessage(chats=[155836063]))
async def replier(event):
	await event.forward_to("@Processing_meaallh")
	


client.run_until_disconnected()
