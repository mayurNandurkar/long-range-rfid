from serial import serialwin32
from time import sleep
import requests

com = serialwin32.Serial('COM3',baudrate=115200,timeout=3)

# print (com.baudrate)
# print(com)

cmd = [0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E]  # Command to Read Tag Once

# print(cmd)
com.flush()
scan = 0

while scan == 0:

    cmd_len = com.write(cmd[0:7])  # Write desired elements at serial port

    data = com.read(size=20)    # Take first 20 bytes of received bytes

    str1 = list(data)       # convert to List

    # list_output = ' '.join( [ "%02X" % ord( x ) for x in str1])
    list_output = ' '.join(["%02X" % ord(x) for x in str1])

    new_list = list_output.split()

    # print("new_list :: ", new_list[8:20])

    new_list = ' '.join(new_list[8:20])

    cmp_data = '30 08 33 B2 DD D9 01 40 00 00 00 00'

    if (new_list == cmp_data):
        print("Data matched : \n")
        # print("new list type '\n")
        print(new_list)
        num = new_list
        userdata = {"epc": num}
        # resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php',params=userdata)
        # print(resp.content)
        scan = 1

com.close()
