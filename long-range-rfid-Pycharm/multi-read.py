from serial import serialwin32
from time import sleep
import requests

com = serialwin32.Serial('COM3',baudrate=115200,timeout=3)

# print (com.baudrate)
# print(com)

cmd_s = [0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E]

cmd_m = [0xBB, 0x00, 0x27, 0x00, 0x03, 0x22, 0x27, 0x10, 0x83, 0x7E ]


# print(cmd)
com.flush()

clen = com.write(cmd_m)       #Write desired command at serial port


while 1:
    count = 0
    data = com.read(size=20)

    str1 = list(data)

    # list_output = ' '.join( [ "%02X" % ord( x ) for x in str1])
    list_output = ' '.join(["%02X" % ord(x) for x in str1])

    # list_output=[hex(ord(x))[2:] for x in str1]

    new_list = list_output.split()
    # print("new_list :: ", new_list[8:20])
    new_list = ' '.join(new_list[8:20])

    print(new_list)
    com.flushInput()
    # cmp_data = '30 08 33 B2 DD D9 01 40 00 00 00 00'
    #
    # if new_list == cmp_data:
    #     # print("Data matched : \n")
    #     # print("new list type '\n")
    #     print("Data Matched:", new_list)
    #     # num = new_list
    #     # userdata = {"epc": num}
    #     # resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php',params=userdata)
    #     # print(resp.content)
    #     # scan = 1
    #
    # # resp = requests.post('http://yourserver.de/test.php', params=userdata)

com.close()
