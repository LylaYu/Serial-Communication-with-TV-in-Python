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
ser = serial.Serial('/dev/ttyUSB0')
enable = "\x8C\x00\x01\x02\x01\x90"
power_on = "\x8C\x00\x00\x02\x01\x8F"
power_off = "\x8C\x00\x00\x02\x00\x8E"
enter = "\x8C\x00\x67\x03\x01\x65\x5C"
home = "\x8C\x00\x67\x03\x01\x60\x57"
left = "\x8C\x00\x67\x03\x01\x34\x2B"
right = "\x8C\x00\x67\x03\x01\x33\x2A"
down = "\x8C\x00\x67\x03\x01\x75\x6C"
up = "\x8C\x00\x67\x03\x01\x74\x6B"

ser.write(enable)
is_on = 0
ser.write(power_on)
is_on = 1
time.sleep(3)
# find burn-in picture
i_l = 5
while i_l:
        ser.write(left)
        time.sleep(1)
        i_l-=1
ser.write(up)
time.sleep(1)
ser.write(right)
time.sleep(1)
i_e = 3
while i_e:
        ser.write(enter)
        time.sleep(1)
        i_e-=1
#time.sleep(28800)
#ser.write(power_off)
#is_on = 0

