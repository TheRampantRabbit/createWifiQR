# createWifiQR

When run will output a QR code as a PNG that when scanned will give the user the option to join the wireless network.

Can be run interactively or with command-line arguments

## Requires
pyqrcode - https://pypi.org/project/PyQRCode/

## Sample usage

### Display Help

```
% python3 joinWifiQR.py -h
usage: joinWifiQR.py [-h] -s SSID -e {WPA,WEP} -p PSK

Generates a QR code that can be used to join a wireless network and output PNG to working directory.

optional arguments:
  -h, --help            show this help message and exit
  -s SSID, --ssid SSID  SSID
  -e {WPA,WEP}, --encr {WPA,WEP}
                        Encryption type, either WEP or WPA (case sensitive)
  -p PSK, --psk PSK     PSK
```

### Create a QR code

The following will output a QR code for a wireless network named MySSID with WPA and a PSK of MyPSK

```
python3 createWifiQR.py -s MySSID -e wpa -p MyPSK
```

Alternatively if it is run without arguments then input will be prompted.
