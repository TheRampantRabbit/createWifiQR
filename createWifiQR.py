import argparse
import pyqrcode


def make_qr(ssid: str, encr: str, psk: str):
    """
    Generates a QR code and outputs a PNG to the working directory and the console using the provided input.

    :param ssid: SSID of the wireless network.
    :param encr: Encryption type (WPA or WEP).
    :param psk: PSK (Pre-Shared Key) for the network.
    """
    encr_str = f'T:{encr}' if encr else ''
    psk_str = f'P:{psk}' if psk else ''
    qr_code = pyqrcode.create(f'WIFI:S:{ssid};{encr_str};{psk_str};;')

    qr_code.png(f'Join_{ssid}.png', scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    print(qr_code.terminal(quiet_zone=1))


def get_user_input():
    """
    Prompts the user for input (SSID, Encryption type, PSK) and generates the QR code with the provided input.
    """
    ssid = input("Enter SSID: ")

    encr_choices = ["WPA", "WEP"]
    encr = input("Enter Encryption type (WPA/WEP) or leave blank: ").upper()
    while encr not in encr_choices and encr:
        encr = input("Invalid Encryption type. Please enter WPA, WEP, or leave blank: ").upper()

    psk = input("Enter PSK or leave blank: ")

    print("\nGenerating a QR Code with the following settings:")
    print(f"SSID: {ssid}")
    print(f"Encryption: {encr}" if encr else "No encryption")
    print(f"PSK: {psk}" if psk else "No PSK")

    proceed = input("Is this correct? (y/n): ")

    if proceed.lower() == "y":
        make_qr(ssid, encr, psk)
    else:
        get_user_input()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    # create arguments
    parser = argparse.ArgumentParser(
        description="Generates a QR code that can be used to join a wireless network and output PNG to the working directory."
    )
    parser.add_argument("-s", "--ssid", required=False, type=str, help="SSID")
    parser.add_argument(
        "-e", "--encr", choices=["WPA", "WEP"], required=False, type=str.upper, help="Encryption type, either WEP or WPA"
    )
    parser.add_argument("-p", "--psk", required=False, type=str, help="PSK")

    # parse arguments and assign
    args = parser.parse_args()

    # check input with the user
    get_user_input()
