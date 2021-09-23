import argparse
import pyqrcode

def main(wifiSSID, wifiEncryption, wifiPSK):
    """ Main entry point of the app """
    QRCode = pyqrcode.create(f'WIFI:S:{wifiSSID};T:{wifiEncryption};P:{wifiPSK};;')
    
    QRCode.png(f'Join_{wifiSSID}.png', scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    # QRCode.show()

    print(QRCode.terminal(quiet_zone=1))

if __name__ == "__main__":
    """ This is executed when run from the command line """

    def checkInput(ssid, encr, psk):
        print("\n")
        print("Generating a QR Code with the following settings:\n")
        print(f"SSID: {ssid}")
        print(f"Encryption: {encr}")
        print(f"PSK: {psk}")
        proceed = input("Is this correct? (y/n): ")

        if proceed != "y":
            ssid = None
            encr = None
            psk = None

            ssid = input("Enter SSID: ")
            while encr not in ("WPA","WEP"):
                encr = input("Enter Encryption (WPA/WEP): ")
            psk = input("Enter PSK: ")

            checkInput(ssid, encr, psk)
        else:
            main(ssid, encr, psk)
    
    parser = argparse.ArgumentParser(description="Generates a QR code that can be used to join a wireless network and output PNG to working directory.")
    parser.add_argument("-s","--ssid", required=True, type=str, help="SSID")
    parser.add_argument("-e","--encr", choices=["WPA","WEP"], required=True, type=str, help="Encryption type, either WEP or WPA (case sensitive)",)
    parser.add_argument("-p","--psk", required=True, type=str, help="PSK")

    args = parser.parse_args()
    ssid = args.ssid
    encr = args.encr
    psk = args.psk

    checkInput(ssid, encr, psk)