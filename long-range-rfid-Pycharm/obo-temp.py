from serial import serialwin32
from time import sleep
import requests

com = serialwin32.Serial('COM3',baudrate=115200,timeout=3)

cmd_s = [0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E]

cmd_m = [0xBB, 0x00, 0x27, 0x00, 0x03, 0x22, 0x27, 0x10, 0x83, 0x7E ]
cmd_mstop = [0xBB, 0x00, 0x28, 0x00, 0x00, 0x28, 0x7E]

count = 0
# print(cmd)
com.flush()

com.write(cmd_m)       #Write desired command at serial port

# try:
while 1:
    if com.isOpen() == False:
        com = serialwin32.Serial('COM3', baudrate=115200, timeout=3)
        com.write(cmd_m)  # Write desired command at serial port

    data = com.readable()

    str1 = list(data)

    # list_output = ' '.join( [ "%02X" % ord( x ) for x in str1])
    list_output = ' '.join(["%02X" % ord(x) for x in str1])

    # list_output=[hex(ord(x))[2:] for x in str1]
    new_list = list_output.split()
    # print("new_list :: ", new_list[8:20])
    new_list = ' '.join(new_list[8:16])
    # cmp_data = '30 08 33 B2 DD D9 01 40 00 00 00 00'
    # cmp_data = '01 12 06 00 00 00 00 21'
    tag_1 = '01 12 06 00 00 00 00 20'
    tag_2 = '02 12 06 00 00 00 00 21 50'
    if new_list == tag_1 or new_list == tag_2:
        # print("Data matched : \n")
        # print("new list type '\n")
        print("Data Matched:", new_list)
        num = new_list
        userdata = {"epc": num}
        # resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php',params=userdata)
        # print(resp.content)
        sleep(2)
        com.flush()
        count += 1
        print(count)
        # com.write(cmd_m)  # Write desired command at serial port
    com.close()



