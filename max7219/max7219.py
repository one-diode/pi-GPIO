#!/usr/bin/env python3

import wiringpi as wp

DIN = 14
CS  = 15
CLK = 18

wp.wiringPiSetup()

wp.pinMode(DIN,1)
wp.pinMode(CS,1)
wp.pinMode(CS,1)

def output(addr,dat):
    wp.digitalWrite(addr,dat)

def max7219_write_byte(dat):
    for i in range(8):
        output(CLK,0)
        output(DIN,dat&0x80)
        dat = dat << 1
        output(CLK,1)
        
def write_max7219(addr,dat1,dat2,dat3,dat4)
    output(CS,0)
    write_max7219_byte(addr)
    write_max7219_byte(dat1)
    write_max7219_byte(dat2)
    write_max7219_byte(dat3)
    write_max7219_byte(dat4)
    output(CS,1)

def init_max7219()
    write_max7219(0x09,0,0,0,0) #译码方式不译码
    write_max7219(0x0a,3,3,3,3) #亮度
    write_max7219(0x0b,7,7,7,7) #扫描界限
    write_max7219(0x0c,1,1,1,1) #掉电模式 0为掉电，1为正常
    write_max7219(0x0f,0,0,0,0) #显示测试：1,测试，0,正常



print ("star")

while 1:
    pass



