import senderConfig as sc
from Sender import *

sender = Sender(sc.rpi_temp_sender)
sender.initialize()
sender.send()