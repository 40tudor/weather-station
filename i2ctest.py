# i2ctest.py
# https://www.sparkfun.com/products/8736

import smbus
import struct
import time

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  MCP4725 defaults to address 0x60
address = 0x60

# Register addresses (with "normal mode" power-down bits)
reg_write = 0xC0
reg_read = 0xC1
Padc_MSB = 0x00
Padc_LSB = 0x01
Tadc_MSB = 0x02
Tadc_LSB = 0x03
a0_MSB = 0x04
a0_LSB = 0x05
b1_MSB = 0x06
b1_LSB = 0x07
b2_MSB = 0x08
b2_LSB = 0x09
c12_MSB = 0x0A
c12_LSB = 0x0B
reg_convert = 0x12


# Initialize I2C (SMBus)
bus = smbus.SMBus(1)

bus.write_i2c_block_data(address, reg_convert, [1])

time.sleep(1)

data=bus.read_i2c_block_data(address, a0_MSB, 2)
(data_s,)=struct.unpack('h', bytearray(data)[0:2])
print "{0:b}".format(data_s)
data_a=float(int(data_s))/4
print data_a

data=bus.read_i2c_block_data(address, b1_MSB, 2) 
(data_s,)=struct.unpack('h', bytearray(data)[0:2]) 
print "{0:b}".format(data_s) 
data_b1=float(int(data_s))/2**12 
print data_b1

data=bus.read_i2c_block_data(address, b2_MSB, 2)
(data_s,)=struct.unpack('h', bytearray(data)[0:2])
print "{0:b}".format(data_s) 
data_b2=float(int(data_s))/2**14
print data_b2

data=bus.read_i2c_block_data(address, c12_MSB, 2) 
(data_s,)=struct.unpack('h', bytearray(data)[0:2]) 
print "{0:b}".format(data_s) 
data_c12=float(int(data_s))/2**22 
print data_c12

data=bus.read_i2c_block_data(address, Tadc_MSB, 2)
print data
data_T=map(bin,data)
print data_T
data_T=int("".join(map(bin,data)))
print "{0:b}".format(data_T)

data=bus.read_i2c_block_data(address, Padc_MSB, 2)
#data = [0,0,0,0,0,0] + data
print data
data_P=int("".join(map(str,data)))
print "{0:b}".format(data_P)

