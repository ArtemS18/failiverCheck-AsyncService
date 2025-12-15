import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TOKEN = os.getenv("SERVICE_TOKEN")
print(WEBHOOK_URL, TOKEN)
