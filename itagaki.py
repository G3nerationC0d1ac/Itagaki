#!/usr/bin/env python3

from datetime import datetime as dtt
import getopt, socket, sys
from requests import get
import pyfiglet as pfgt
import time, os

"""

Made by C0d1ac with <3 

TCP Portscanner - Itagaki
--------------------------------------------------------------------
Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>

"""


def main(argv):
    target_host = ""
    target_port = ""

    try:
        opts, args = getopt.getopt(
            argv,
            "ht:m:",
            [
                "thost=",
                "mport="
            ]
        )
    except getopt.GetoptError:
        print("Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>")
        sys.exit(1)

    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>")
                sys.exit(0)
                
            elif opt in ("-t", "--thost"):
                target_host = arg
            elif opt in ("-m", "--mport"):
                target_port = arg
            else:
                print("Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>")
                sys.exit(0)
                
    except ValueError:
        print("Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>")
        sys.exit(0)

    infob = [
        f"\033[0;37mCodiac",
        "1.0.1",
    ]

    name     = f"\033[0;31m" + infob[0]
    vers     = f"\033[0;31m" + infob[1]
    start_t  = dtt.now()
    get_addr = socket.gethostbyname(target_host)
    line_    = f"\033[0;31m-" * 55

    os.system("clear")

    print(
        "\033[0;31m", pfgt.figlet_format(
            "Itagaki",
            font="slant"
        ) + f"\033[0;37m"
    )

    print("\033[0;31m-" * 55)
    print(f" Author: {name}\t\t\t\n Ver.: {vers}")
    print("\n \033[0;37m{\033[0;31m*\033[0;37m} ", f"Start scan at => {start_t}")

    time.sleep(1)

    print(" \033[0;37m{\033[0;31m*\033[0;37m\033[0;37m} ", f"Scan range => 0 - {target_port}")

    time.sleep(1)

    print(" \033[0;37m{\033[0;31m*\033[0;37m} ", f"Start scanning target => {target_host}/{get_addr}")

    time.sleep(1)

    print(f"\n \033[0;37mProtocol\tPort\tStatus\t\t Service\n{line_}")

    try:
        for target in range(
                1,
                int(target_port)
        ):
            with socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
            ) as socket_sock:
                final_result = socket_sock.connect_ex((
                    target_host,
                    target
                ))

                socket_sock.settimeout(1)
                
                if final_result == 0:
                    try:
                        print(
                            f" \033[0;36m[\033[0;31m+\033[0;36m] \033[0;32mTCP  \t{target}\topen\t\t",
                            socket.getservbyport(target)
                        )
                    except socket.error:
                        print(f" \033[0;36m[\033[0;31m+\033[0;36m] \033[0;32mTCP  \t{target}\topen\t\t Unknown")

                socket_sock.close()
                
    except socket.error:
        pass
    except ValueError:
        print("Usage: python3 codiacScan.py -t <target_host> -m <maximum_port>")
        sys.exit(0)
    except KeyboardInterrupt:
        print(f"\n \033[0;31mCtrl+C pressed.")
        sys.exit(0)

    end_t = dtt.now()
    needed_time = end_t - start_t

    print("\n \033[0;37m{\033[0;31m*\033[0;37m} ", f" Codiac PortScanner done in {needed_time}")


if __name__ == "__main__":
    print(f"Remember, your public ip address is {get('https://api.ipify.org').text}.")

    r_sure = input(f"Do you want to start scanning? y/n ")
    
    if r_sure == 'y' or r_sure == 'Y':
        pass
    elif r_sure == 'n' or r_sure == 'N':
        sys.exit(0)
    else:
        print(f"\033[0;31mInvalid Input!")
        sys.exit(0)

    main(sys.argv[1:])
