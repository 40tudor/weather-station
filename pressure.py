#!/usr/bin/env/python

import smbus
import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.25)
unicorn.rotation(0)

display=[ ([0] * 8) for row in range(4) ]

setup i2c

shift_display():
   for i in range(len(display)):
      for j in range(len(display[i]):
         display[i,j]=display[i+1,j]

get pressure
scale 0-4
store in display_array

for y in xrange(0, 4):
   for x in xrange(0, 8)
      unicorn.set_pixel(x,y,Color)
unicorn.show()

shift array

wait 60 min

interrupt pushbutton to switch between temperature and pressure?
