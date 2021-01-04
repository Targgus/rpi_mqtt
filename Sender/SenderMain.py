import senderConfig as sc
from Sender import *
import time

sender = Sender(sc.rpi_all_sender)
sender.initialize()
while True:
    sender.send()
    time.sleep(10)