#!/usr/bin/env python
# coding=utf-8
from app import app 
app.run(debug=True)
#from app import Productor,Consumer
#from app import g_cusEvent,g_proEvent
#from app import time
#if __name__ == '__main__':
    
#    p = Productor(g_cusEvent,g_proEvent)
#    c = Consumer(g_cusEvent,g_proEvent)
#    p.start()
#    c.start()
#    time.sleep(3)
#    g_cusEvent.set()
#    p.join()
#    c.join()
