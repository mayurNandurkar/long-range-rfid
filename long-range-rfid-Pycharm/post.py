
import requests

mac="123456789"
epc_n="0102050000000021"
rfid_n="E28011702000049E50"

# userdata = {"epc": epc_n, "rfid": rfid_n, 'mac_address': mac}

data = {"mac_address": mac, "rfid":rfid_n,"epc":epc_n}
resp = requests.post('http://104.37.185.20/~tech599/tech599.com/johnaks/flowers_new/inventory/api/read_tag.php',params=data)
print "mac address " , resp.content