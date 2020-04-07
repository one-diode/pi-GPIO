#!/usr/bin/env python3

import _thread,time

def getkey(threadname):
    while 1:
        str = input("%s请输入:\n"%threadname)
        print("%s 你输入的值是:%s"%(threadname,str))


try:
    _thread.start_new_thread(getkey,("th1",))
except:
    print("无法启动线程")

while 1:
    print("当前时间:"+time.ctime(time.time()))
    time.sleep(1)

