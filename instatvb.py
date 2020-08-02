#/bin/python3.8
from instabot import InstaBot as bot
import env


b=bot(login=env.USER,password=env.PASS)

print('logged-in')

b.logout()

print('logged-out')