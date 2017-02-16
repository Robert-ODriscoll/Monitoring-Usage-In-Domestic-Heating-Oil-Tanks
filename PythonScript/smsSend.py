#!/usr/bin/python

from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

phoneNumber = input('0838184277')
text = input('Message text: ')

voice.send_sms(phoneNumber, text)
