from totp import TotpHandler
from dotenv import load_dotenv
import os

load_dotenv()

totp_handler = TotpHandler(secret=os.getenv("GH_SECRET"))
