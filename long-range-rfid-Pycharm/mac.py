def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
    # str = "23:45:45:66:23:89"
  return str[0:17]

mac=getMAC()
print mac