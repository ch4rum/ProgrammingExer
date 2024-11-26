
import os
import getpass
import base64
import signal
from colorama import Fore, Style, init  
from Crypto.Random import get_random_bytes

from DBs.conectDB import ConnectDB
from srcH.writeOutput import WriteObj

class Menus(WriteObj):

    def __init__(self: 'Menus') -> None:
        self.pc_user = os.getlogin()
        self.THIS_VERSION = 1.1
        self.db_app = None
        signal.signal(signal.SIGINT, self.shutdownsdb)

    def _login_db(self):
        try:
            self.print_debug(" ",f"\n\t\t{Fore.LIGHTCYAN_EX}.:LOGIN DATABASE:.\n")
            username = input(f"{Fore.LIGHTMAGENTA_EX}Username{Fore.GREEN}:{Style.RESET_ALL} ")
            password = base64.b64encode(getpass.getpass(f"{Fore.LIGHTMAGENTA_EX}Password{Fore.GREEN}:{Style.RESET_ALL} ").encode('utf-8')).decode('utf-8') 
            if not password:
                raise ValueError("La contraseña no puede estar vacía.")
            encryption_key = get_random_bytes(16)
            self.db_app = ConnectDB(username, password, encryption_key)
        except Exception as e:
            self.print_debug(" ","")
            self.print_debug("FAILED", f"{e}\n")
            exit(1)

    def shutdownsdb(self, signum, frame):
        self.print_debug(" ", "\n")
        self.print_debug("WARNING","Close SQL server...\n")
        if self.db_app:
            self.db_app.close()
        exit(0) 

    def print_banner(self):
        banner =f"""                                  

          {Fore.LIGHTRED_EX}  [.. ..      [....    [..                       
          {Fore.LIGHTRED_EX}[..    [..  [..    [.. [..                       
          {Fore.LIGHTRED_EX} [..      [..       [..[..      [. [..  [..   [..    {Fore.GREEN}│ {Fore.WHITE}By: Ch4rum
          {Fore.LIGHTRED_EX}   [..    [..       [..[..      [.  [..  [.. [..     {Fore.GREEN}├────────────
          {Fore.LIGHTRED_EX}      [.. [..       [..[..      [.   [..   [...      {Fore.GREEN}│ {Fore.WHITE}Running on: {self.pc_user} PC
          {Fore.LIGHTRED_EX}[..    [..  [.. [. [.. [..      [.. [..     [..      {Fore.GREEN}├────────────
          {Fore.LIGHTRED_EX}  [.. ..      [.. ..   [........[..        [..       {Fore.GREEN}│ {Fore.WHITE}v{self.THIS_VERSION}
          {Fore.LIGHTRED_EX}                   [.           [..      [..  """
        self.print_debug(" ", banner)

    def print_options(self):
        r = Fore.RED
        g = Fore.GREEN
        lb = Fore.LIGHTBLUE_EX
        reset = Style.RESET_ALL
        options = f"""{lb}
            ╭────────────[ Opciones de SQL ]────────────────╮
            │                                               │
            │    Selecciona la base de datos [1-9]          │
            │                                               │
            │    {r}⦿{lb} {g}→{lb} DbLab                                  │ 
            │    {r}⦿{lb} {g}→{lb} DbLabTwo                               │  {r}[>]{lb} {g}→{lb} Menu
            │                                               │  {r}[!]{lb} {g}→{lb} Salir 
            ╰───────────────────────────────────────────────╯
    {reset}"""
        self.print_debug(" ",options)

    def choose_option(self: 'Menus') -> None:
        while True:
            choice = input(f'{Fore.BLUE}  {Fore.MAGENTA}{self.pc_user}{Fore.RED}@{Fore.BLUE}DB_SQLpy{Fore.BLACK}~{Fore.GREEN}  {Fore.CYAN}').upper()
            try :
                options = {
                    '1': self.main_menu_one,
                    '2': self.main_menu_two,
                    '>': self.main_menu,
                    '!': exit
                }
                chosen = options.get(choice)
                if chosen: 
                    chosen()
                else :
                    self.print_debug(" ", "")
                    self.print_debug("WARNING",f"Invalid choice, please try again!\n")
            except Exception as err:
                self.print_debug("ERROR",f"Error: {err}\n")

    def main_menu_one(self):
        try:
            from Menus.MenuOne import MenuOne 
            menuOne = MenuOne(self.db_app)
            menuOne.main_menu_one()
        except Exception as err:
            self.print_debug("ERROR", f"Error: {err}\n")

    def main_menu_two(self):
        try:
            from Menus.MenuTwo import MenuTwo
            menuTwo = MenuTwo(self.db_app)
            menuTwo.main_menu_two()
        except Exception as err:
            self.print_debug("ERROR", f"Error: {err}\n")

    def main_menu(self: 'Menus') -> None:
        self._login_db()
        os.system("cls" if os.name == 'nt' else "clear")
        self.print_banner()
        self.print_options()
        self.choose_option()
