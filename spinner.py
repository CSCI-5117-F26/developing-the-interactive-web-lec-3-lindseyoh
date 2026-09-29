import time
from halo import Halo


spinner = Halo(text='buhbuhbuhbuh', spinner='dots')
spinner.start()
time.sleep(60)

spinner.stop()

