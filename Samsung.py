import serial
ser = serial.Serial('/dev/ttyUSB0')

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
command_on = "\x08\x22\x00\x00\x00\x02\xD4"
command_off = "\x08\x22\x00\x00\x00\x01\xD5"
left = "\x08\x22\x0D\x00\x00\x65\x64"
up = "\x08\x22\x0D\x00\x00\x60\x69"
right = "\x08\x22\x0D\x00\x00\x62\x67"
menu = "\x08\x22\x0D\x00\x00\x1A\xAF"
enter = "\x08\x22\x0D\x00\x00\x68\x61"
send = 0
ser.write(command_on)
time.sleep(3)
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
#ser.write(command_off)