from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
REC_EMAIL = os.getenv("REC_EMAIL")
PWD_APP = os.getenv("PWD_APP")
FLICKR_API_KEY = os.getenv("FLICKR_API_KEY")
FLICKR_API_SECRET = os.getenv("FLICKR_API_SECRET")
FLICKR_USER_ID = os.getenv("FLICKR_USER_ID")
API_COVID = os.getenv("API_COVID")