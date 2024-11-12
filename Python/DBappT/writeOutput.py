from termcolor import colored

class WriteObj:
    
    def print_debug(self, error: str, message: str, end="\n") -> None:
        error_level = {"OK":colored(f"[+] {message}","green"),
                       "FAILED":colored(f"[x] {message}","blue"),
                       "ERROR":colored(f"[-] {message}","red"),
                       "WARNING":colored(f"[!] {message}","yellow"),
                       " ": f"{message}"}
        
        print(error_level.get(error, f"{message}"), end=end)

# Ejemplo de uso
#obj = WriteObj()
#obj.print_debug("OK", "Operation successful")
#obj.print_debug("FAILED", "Operation failed")
#obj.print_debug("ERROR", "Critical error occurred")
#obj.print_debug("WARNING", "This is a warning")