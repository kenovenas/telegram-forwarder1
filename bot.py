from telethon import TelegramClient, events

# Substitua com seu próprio API ID e Hash
api_id = 20225004
api_hash = '8f4c78e858658cd2aa21967a087bf819'
session_name = 'forwarder'

# IDs dos grupos
source_chat_id = -1002590813877
target_chat_id = -1002656975250

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_chat_id))
async def handler(event):
    await client.send_message(target_chat_id, event.message)

print("Bot rodando...")
client.start()
client.run_until_disconnected()
