#!/usr/bin/env python3

import argparse
import sys
import signal
from scanICMP import ICMPscan
from scanPort import ScannerPort

def ctrl_c(sig, frame):
    print("\n[!] Exiting...")
    sys.exit(1)
    
signal.signal(signal.SIGINT, ctrl_c)

def args_Argument():
    try:
        p = argparse.ArgumentParser(prog="scanICMP.py", description="Tool to discover active hosts on an ICMP network.")
        p.add_argument("-t","--target",
                       dest="target",
                       required=True,
                       metavar="<target>",
                       type=str,
                       help="Host or range of network to scan.")
        p.add_argument("-p","--port",
                       dest="port",
                       type=str,
                       metavar="<ports>",
                       required=True,
                       help="Port ranget to scan (Ex: 22 or 22,80,443 or 20-10000)")
        options = p.parse_args()
        if (options.port is None or options.target is None) or len(sys.argv) == 1:
            parse.print_help()
            sys.exit(1)
        return options.target, options.port
    except argparse.ArgumentError:
        print("\n[-] Error Argument.\n")
        sys.exit(1)

if __name__ == "__main__":
    target_str, ports_str = args_Argument()
    scaning = ICMPscan(target_str)
    active_host = scaning.start()
    print(f"\n[+] Hosts actives in the network:")
    for ip in active_host:
        print(f"\t[i] The IP {ip} - ACTIVE")
        scaningPort = ScannerPort(ip,ports_str)
        scaningPort.start()
    if len(active_host) == 0:
        print("\t[i] There is no active host")