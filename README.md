# Long Range Rfid
This repo contains python scripts to handle the long range UHF RFID reader.

Long ramge UHF rfid reader operates in two modes.
# 1. Single Read
# 2. Multi Read

In Single read, when a read command is send to reader , it will read one tag present in front of it.
In Multi read mode, when a read command is send to reader, it continuosly reads all the RFID tags 
present in front of it. It will read same RFID tag for multiple times as well.

Changes are as when a read command is sent , receiver read first RFID tag number and discards remaining.

Finally is displays Scanned RFID card with EPC number.
