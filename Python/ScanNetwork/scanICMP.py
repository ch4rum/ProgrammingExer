
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

class ICMPscan:
    
    def __init__(self, target):
        self.target = self.parse_target(target)
        self.active_host = []
        
    def start(self):
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.host_discovery, self.target)
        return self.active_host
        
    def host_discovery(self, target):
        try:
            ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
            if ping.returncode == 0:
                self.active_host.append(target)
        except subprocess.TimeoutExpired:
            pass
    
    def parse_target(self, target_str):
        target_str_split = target_str.split(".")
        first_three_octets = '.'.join(target_str_split[:3])
        if len(target_str_split) == 4:
            if '-' in target_str_split[3]:
                start, end = target_str_split[3].split('-')
                if int(start) >= 1 and int(end) <= 255:
                    if int(end) == 255:
                        end = 254
                    return [f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1)]
                else:
                    print("\n[-] Range IP not valid.")
            else:
                return[target_str]
        else:
            print("\n[-] The format IP not valid.")
    