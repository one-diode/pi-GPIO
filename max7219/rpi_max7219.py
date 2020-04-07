#!/usr/bin/env python3

import RPi.GPIO as GPIO
import threading
import ascii_8x8 as font

DIN = 14
CS  = 15
CLK = 18

chan = (DIN,CS,CLK)

GPIO.setmode(GPIO.BCM)
GPIO.setup(chan,GPIO.OUT,initial=GPIO.LOW)



def output(addr,dat):
    GPIO.output(addr,dat)

def max7219_write_byte(dat):
    for i in range(8):
        output(CLK,0)
        output(DIN,dat&0x80)
        dat = dat << 1
        output(CLK,1)

def write_max7219(addr,dat1,dat2,dat3,dat4):
    output(CS,0)
    max7219_write_byte(addr)
    max7219_write_byte(dat1)
    max7219_write_byte(addr)
    max7219_write_byte(dat2)
    max7219_write_byte(addr)
    max7219_write_byte(dat3)
    max7219_write_byte(addr)
    max7219_write_byte(dat4)
    output(CS,1)

def max7219_clean():
    for i in range(8):
        write_max7219(i+1,0,0,0,0)

def max7219_all():
    for i in range(8):
        write_max7219(i+1,255,255,255,255)

def show_ascii(dat):
    dat = list(dat)
    for i in range(8):
        if len(dat) == 1:
            write_max7219(i+1,font.ascii[dat[0]][i],0,0,0)
        elif len(dat) == 2:
            write_max7219(i+1,font.ascii[dat[0]][i],font.ascii[dat[1]][i],0,0)
        elif len(dat) == 3:
            write_max7219(i+1,font.ascii[dat[0]][i],font.ascii[dat[1]][i],font.ascii[dat[2]][i],0)
        elif len(dat) >= 4:
            write_max7219(i+1,font.ascii[dat[0]][i],font.ascii[dat[1]][i],font.ascii[dat[2]][i],font.ascii[dat[3]][i])

def init_max7219():
    write_max7219(0x09,0,0,0,0) #译码方式不译码
    write_max7219(0x0a,1,1,1,1) #亮度
    write_max7219(0x0b,7,7,7,7) #扫描界限
    write_max7219(0x0c,1,1,1,1) #掉电模式 0为掉电，1为正常
    write_max7219(0x0f,0,0,0,0) #显示测试：1,测试，0,正常

def getcmd(threadName):
    while 1:
        cmd = input("输入指令:")
        if cmd == 'q':
            GPIO.cleanup()
            exit()
        elif cmd == 'ld':
            ld = int(input("请输入亮度级别(0-15):"))
            write_max7219(0x0a,ld,ld,ld,ld)
        elif cmd == 'cs':
            write_max7219(0x0f,1,1,1,1)
        elif cmd == 'off':
            write_max7219(0x0c,0,0,0,0)
        elif cmd == 'nor':
            write_max7219(0x0c,1,1,1,1)
            write_max7219(0x0f,0,0,0,0)
        elif cmd == 'all':
            max7219_all()
        elif cmd == 'clean':
            max7219_clean()
        else:
            print("你输入的是:%s"%cmd)
            show_ascii(cmd)

def ceshi():
    str = input("asc:")
    print (font.ascii[str])

init_max7219()

while 1:
    getcmd(1)
    #ceshi()


