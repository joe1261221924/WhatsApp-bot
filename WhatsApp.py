import asyncio
from pyrogram import Client, filters

# Initialize your Pyrogram client (you can use your own API credentials)
api_id = "your_api_id"
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.private)
async def handle_message(client, message):
    # Respond to incoming messages
    await message.reply_text("Hello! I am your WhatsApp bot.")

@app.on_user_status()
async def handle_status(client, status):
    # Automatically view statuses
    print(f"User {status.user_id} updated status: {status.status}")

async def main():
    await app.start()
    await app.idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
