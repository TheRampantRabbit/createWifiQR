import argparse
import pyqrcode

def makeQR(ssid, encr, psk):
    """ function outputs a png to working directory and to console using input provided """
    
    ssid = f'S:{ssid}'

    if not encr:
        encr = ""
    else:
        encr = f'T:{encr}'

    if not psk:
        psk = ""
    else:
        psk = f'P:{psk}'

    QRCode = pyqrcode.create(f'WIFI:{ssid};{encr};{psk};;')
    
    QRCode.png(f'Join_{ssid}.png', scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    # QRCode.show()

    print(QRCode.terminal(quiet_zone=1))

def checkInput(ssid, encr, psk):
    """
    function to check user input before generating QR code
    """
    # print user input to console
    if ssid:
        print("\n")
        print("Generating a QR Code with the following settings:\n")
        print(f"SSID: {ssid}")
        print(f"Encryption: {encr}")
        print(f"PSK: {psk}")
        proceed = input("Is this correct? (y/n): ")
        print("\n")
    else:
        # will prompt for input if the SSID entered
        proceed = False

    # if input is incorrect null the variables and prompt for input
    if proceed != "y":
        ssid = None
        encr = None
        psk = None

        while not ssid:
            ssid = input("Enter SSID: ")
        while encr not in ("WPA","WEP",""):
            encr = str.upper(input("Enter Encryption type WPA/WEP or leave blank: "))
        if encr == "":
            encr = None
        psk = input("Enter PSK or leave blank: ")
        if psk == "":
            psk = None

        # re-check user input
        checkInput(ssid, encr, psk)
    else:
        # make the QR code
        makeQR(ssid, encr, psk)

if __name__ == "__main__":
    """ This is executed when run from the command line """
            
    # create arguments
    parser = argparse.ArgumentParser(description="Generates a QR code that can be used to join a wireless network and output PNG to working directory.")
    parser.add_argument("-s","--ssid", required=False, type=str, help="SSID")
    parser.add_argument("-e","--encr", choices=["WPA","WEP"], required=False, type=str.upper, help="Encryption type, either WEP or WPA")
    parser.add_argument("-p","--psk", required=False, type=str, help="PSK")

    # parse arguments and assign
    args = parser.parse_args()
        
    # check input with user
    checkInput(args.ssid, args.encr, args.psk)