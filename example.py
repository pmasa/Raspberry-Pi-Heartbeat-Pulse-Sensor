from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()

try:
    while True:
        bpm = p.BPM
        #if bpm > 0:
        if bpm > 220 and bpm < 235:
            print("BPM: %d" % (bpm-170))
        else:
            #print("No Heartbeat found")
            print("BPM: 0")
        time.sleep(1)
except:
    p.stopAsyncBPM()
