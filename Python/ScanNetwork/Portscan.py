#!/usr/bin/env python3

import argparse
import sys
import signal
from scanPort import ScannerPort

def ctrl_c(sig, frame):
    print("\n[!] Exit ...")
    sys.exit(1)
    
signal.signal(signal.SIGINT, ctrl_c)

def get_argument():
    try:
        parse = argparse.ArgumentParser(prog="Portscan.py",
                                        description="Fast TCP port scanner")
        parse.add_argument("-p","--port",
                           dest="port",
                           type=str,
                           metavar="<ports>",
                           required=True,
                           help="Port ranget to scan (Ex: 22 or 22,80,443 or 20-10000)")
        parse.add_argument("-t","--target",
                           dest="target",
                           type=str,
                           metavar="<target>",
                           required=True,
                           help="Victim target to scan")
        options = parse.parse_args()
        if (options.port is None or options.target is None) or len(sys.argv) == 1:
            parse.print_help()
            sys.exit(1)
        return options.target, options.port
    except argparse.ArgumentError:
        print("\n[-] Error argument")

if __name__ == "__main__":
    target, ports_str = get_argument()
    scan = ScannerPort(target, ports_str)
    scan.start()
    
    