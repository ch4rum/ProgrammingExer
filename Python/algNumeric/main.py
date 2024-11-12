#!/usr/bin/env python3

import signal
from Menu import *

def ctrl_c(sig, frame):
    print(f"{Fore.RED}\n\n[!] Saliendo...\n{Style.RESET_ALL}")
    exit(1)

signal.signal(signal.SIGINT, ctrl_c)

if __name__ == "__main__":
    init()
    menu = Menus()
    menu.main_menu()
