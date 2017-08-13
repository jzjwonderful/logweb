#!/usr/bin/env python
# coding=utf-8
from flask import Flask
app = Flask(__name__)
from app import views

from queue import Queue
myQ = Queue()

from threading import Thread, Event
import time

g_cusEvent = Event()   #global event object
g_proEvent = Event()   #global productor event object



class Productor(Thread):
    def __init__(self, consumer_event,productor_event):
        Thread.__init__(self)
        self.consumer_event = consumer_event
        self.productor_event = productor_event

    def run(self):
        id = 1
        while True:
            self.consumer_event.wait()    #等待生产者写入数据
            # 处理数据
            myQ.put("      get %d\n" % id)
            print("put %d \n" % id)
            id += 1
            time.sleep(1)
            self.productor_event.set()
            if not myQ.qsize() > 5:# 如果队列不满则手动重置消费者事件 允许再次插入数据
                self.consumer_event.set()
            else:
                print("queue is full...\n")
        

class Consumer(Thread):
    def __init__(self, consumer_event,productor_event):
        Thread.__init__(self)
        self.consumer_event = consumer_event
        self.productor_event = productor_event

    def run(self):
        while True:
            self.productor_event.wait()
            print (myQ.get())
            time.sleep(4)
            self.consumer_event.set()


        
