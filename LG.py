"""
The whole version of defining ser
ser = serial.Serial( #Serial COM configuration
    port='COM5',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    timeout=2,
    writeTimeout=5
  )"""
import serial
import time
ser0 = serial.Serial('/dev/ttyUSB0')
ser1 = serial.Serial('/dev/ttyUSB1')
ser2 = serial.Serial('/dev/ttyUSB2')
ser3 = serial.Serial('/dev/ttyUSB3')

power_on = "ka 01 01\x0D"
power_off = "ka 01 00\x0D"
#menu = "mc 01 43\x0D"
up = "mc 01 40\x0D"
down = "mc 01 41\x0D"
right = "mc 01 06\x0D"
left = "mc 01 07\x0D"
enter = "mc 01 44\x0D"
#back = "mc 01 28\x0D"
#exit = "mc 01 5b\x0D"
#select_input =  "xb 00 40\x0D"
inp = "mc 00 0B\x0D"

def turn_on(ser):
	ser.write(power_on)
	time.sleep(3)
	ser.write(inp)
	time.sleep(1)
	ser.write(down)
	time.sleep(1)
	ser.write(down)
	time.sleep(1)
	ser.write(enter)
	time.sleep(1)
	ser.write(enter)
	time.sleep(1)
	ser.write(right)
	time.sleep(1)
	ser.write(right)
	time.sleep(1)
	ser.write(enter)
	time.sleep(1)

turn_on(ser0)
turn_on(ser1)
turn_on(ser2)
turn_on(ser3)


