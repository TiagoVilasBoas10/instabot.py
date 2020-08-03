#/bin/python3.8.2
import os
from instabot import InstaBot as bot
from dotenv import load_dotenv
load_dotenv()



b=bot(login=os.getenv("BOTUSER"),password=os.getenv("BOTPASS"))

print('logged-in')

b.logout()

print('logged-out')