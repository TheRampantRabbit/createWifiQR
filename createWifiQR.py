import argparse
import pyqrcode

def makeQR(ssid, encr, psk):
    """ function outputs a png to working directory and to console using input provided """
    QRCode = pyqrcode.create(f'WIFI:S:{ssid};T:{encr};P:{psk};;')
    
    QRCode.png(f'Join_{ssid}.png', scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    # QRCode.show()

    print(QRCode.terminal(quiet_zone=1))

def checkInput(ssid, encr, psk):
    """
    function to check user input before generating QR code
    """
    # print user input to console
    print("\n")
    print("Generating a QR Code with the following settings:\n")
    print(f"SSID: {ssid}")
    print(f"Encryption: {encr}")
    print(f"PSK: {psk}")
    proceed = input("Is this correct? (y/n): ")
    print("\n")

    # if input is incorrect null the variables and prompt for input
    if proceed != "y":
        ssid = None
        encr = None
        psk = None

        ssid = input("Enter SSID: ")
        while encr not in ("WPA","WEP"):
            encr = input("Enter Encryption (WPA/WEP): ")
        psk = input("Enter PSK: ")

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
    parser.add_argument("-e","--encr", choices=["WPA","WEP"], required=False, type=str, help="Encryption type, either WEP or WPA (case sensitive)",)
    parser.add_argument("-p","--psk", required=False, type=str, help="PSK")

    # parse arguments and assign
    args = parser.parse_args()
    
    # check if all arguments were set
    if args.ssid is not None:
        ssid = args.ssid
    else:
        ssid = input("Enter SSID: ")
    
    if args.encr is not None:
        encr = args.encr
    else:
        # set encr to None so while loop does not throw an exception
        encr = None
        while encr not in ("WPA","WEP"):
            encr = input("Enter Encryption (WPA/WEP): ")

    if args.psk is not None:    
        psk = args.psk
    else:
        psk = input("Enter PSK: ")

    # check input with user
    checkInput(ssid, encr, psk)