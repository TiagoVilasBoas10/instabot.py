#/bin/python3.8.2
import os
from instabot import InstaBot as bot
from dotenv import load_dotenv
load_dotenv()


<<<<<<< HEAD
=======

>>>>>>> 1ed5ad104ba74df23148c0b73499bdc16d0db74d
b=bot(login=os.getenv("BOTUSER"),password=os.getenv("BOTPASS"))

print('logged-in')

b.logout()

print('logged-out')