# createWifiQR

## Sample usage

% python3 joinWifiQR.py -h
usage: joinWifiQR.py [-h] -s SSID -e {WPA,WEP} -p PSK

Generates a QR code that can be used to join a wireless network and output PNG to working directory.

optional arguments:
  -h, --help            show this help message and exit
  -s SSID, --ssid SSID  SSID
  -e {WPA,WEP}, --encr {WPA,WEP}
                        Encryption type, either WEP or WPA (case sensitive)
  -p PSK, --psk PSK     PSK
