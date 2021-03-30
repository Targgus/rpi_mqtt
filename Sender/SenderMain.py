import senderConfig as sc
from Sender import *
import time



sender = tempSender()

while True:
    sender.sendTemp()
    time.sleep(10)