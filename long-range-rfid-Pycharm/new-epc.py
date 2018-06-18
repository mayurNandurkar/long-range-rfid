from serial import serialwin32
from time import sleep
import requests

com = serialwin32.Serial('COM3', baudrate=115200, timeout=3)
com.flush()

# print (com.baudrate)
# print(com)

cmd = [0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E]  # Command to Read Tag Once
tag_1 = '01 12 06 00 00 00 00 20'
tag_2 = '02 12 06 00 00 00 00 21'
# print(cmd)
com.flush()
scan = 0
count = 0
while (scan == 0) & (count < 12):

    cmd_len = com.write(cmd[0:7])  # Write desired elements at serial port
    # sleep(0.50)
    data = com.read(size=20)    # Take first 20 bytes of received bytes

    # print(int(data))
    str1 = list(data)       # convert to List
    # list_output = ' '.join( [ "%02X" % ord( x ) for x in str1])
    list_output = ' '.join(["%02X" % ord(x) for x in str1])

    new_list = list_output.split()
    new_list = ' '.join(new_list[8:16])
    if new_list == tag_1 or new_list == tag_2:
        print("Data matched : \n")
        # print("new list type '\n")
        print(new_list)
        num = new_list
        userdata = {"epc": num}
        # resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/api/read_tag.php', params=userdata)
        # print(resp.content)
        # scan = 1
        com.flush()
        count += 1
        sleep(2)

    else:
        print("Tag not matched")
        count += 1
        sleep(2)
        com.flush()         # Even if data is not matched, flush the com serial port.
com.close()
