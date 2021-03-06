from serial import serialwin32
from time import sleep
import datetime
import requests

# from tmp_sense import read_temp
com = serialwin32.Serial('COM3',baudrate=115200,timeout=1)
# print(datetime.datetime.now())
temp = 27.22
# temp = read_temp()

# cmd_s = [0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E]
cmd_tid = [0xBB, 0x00, 0x39, 0x00, 0x09, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x04, 0x48, 0x7E]

# cmd_m = [0xBB, 0x00, 0x27, 0x00, 0x03, 0x22, 0x27, 0x10, 0x83, 0x7E ]
cmd_mstop = [0xBB, 0x00, 0x28, 0x00, 0x00, 0x28, 0x7E]

count = 0
# print(cmd)
com.flush()

com.write(cmd_tid)       #Write desired command at serial port

# try:
while 1:
    if com.isOpen() == False:
        print("Opening port...")
        sleep(1)
        com = serialwin32.Serial('COM3', baudrate=115200, timeout=1)
        com.flushInput()
        com.write(cmd_tid)  # Write desired command at serial port

    data = com.read(size=35)

    str1 = list(data)
    list_output = ' '.join( [ "%02X" % ord( x ) for x in str1])
    list_output = ' '.join(["%02X" % ord(x) for x in str1])
    new_list = list_output.split()
    print("length is : ", len(new_list))

    if len(new_list)==26:
        print(new_list)
        epc_n = ' '.join(new_list[8:16])
        rfid_n = ' '.join(new_list[16:25])
        print("EPC no is :", epc_n, '\n')
        print("TID no is :", rfid_n, '\n')
        print(count)
        userdata = {"epc": epc_n, "temp": temp,"rfid":rfid_n}
        resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php', params=userdata)
        print(resp.content)
    com.flushInput()
    # com.flushOutput()

    # com.flush()
    count += 1
    print(count)
    com.close()

    # com.close()
    # cmp_data = '30 08 33 B2 DD D9 01 40 00 00 00 00'
    # cmp_data = '01 12 06 00 00 00 00 21'
    # tag_1 = '01 12 06 00 00 00 00 20'
    # tag_2 = '02 12 06 00 00 00 00 21'
    # tag_3 = '01 12 06 00 00 00 00 21'
    # tag_4 = '02 12 06 00 00 00 00 20'


