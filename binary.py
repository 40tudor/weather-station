#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.25)
unicorn.rotation(180)

red=255
green=0
blue=0

while 1:
  decimal = time.strftime("%I%M%S")
  decimal_list = list(decimal)

  for x in xrange(0, 6):
    binary = bin(int(decimal_list[x]))[2:].rjust(4, '0')
    binary_list = list(binary)
    if x<=1:
      red=255
      green=0
      blue=0
    elif x==2 or x==3:
      red=0
      green=255
      blue=0
    else:
      red=0
      green=0
      blue=255

    for y in xrange(0, 4):
      if binary_list[y] == '1':
        unicorn.set_pixel(x+1,y,red,green,blue)
      else:
        unicorn.set_pixel(x+1,y,0,0,0)

  unicorn.show()
  time.sleep(1)
