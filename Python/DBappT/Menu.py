
import os
import signal
from database import *
from colorama import Fore, Style, init
from writeOutput import *

class Menus(WriteObj):

    def __init__(self: 'Menus') -> None:
        self.pc_user = os.getlogin()
        self.THIS_VERSION = 1.0
        self.db_app = None
        signal.signal(signal.SIGINT, self.shutdownsdb)
        self._login_db()

    def _login_db(self):
        try:
            self.print_debug(" ",f"\n\t\t{Fore.LIGHTCYAN_EX}.:LOGIN DATABASE:.\n")
            username = input(f"{Fore.LIGHTMAGENTA_EX}Username{Fore.GREEN}:{Style.RESET_ALL} ")
            password = base64.b64encode(getpass.getpass(f"{Fore.LIGHTMAGENTA_EX}Password{Fore.GREEN}:{Style.RESET_ALL} ").encode('utf-8')).decode('utf-8') 
            encryption_key = get_random_bytes(16)
            self.db_app = DBappT(username, password, encryption_key)
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
    ╭───────────────────────────────[ Opciones de SQL ]───────────────────────────────╮
    │                                                                                 │
    │   {r}[1]{lb} {g}→{lb} Insertar Cliente.    │   {r}[a]{lb} {g}→{lb} Listar pedidos fecha resiente.           │ 
    │   {r}[2]{lb} {g}→{lb} Insentar Pedido.     │   {r}[b]{lb} {g}→{lb} Listar pedidos rango 300 y 600.          │ 
    │   {r}[3]{lb} {g}→{lb} Insertar Comercial.  │   {r}[c]{lb} {g}→{lb} Clientes cullo 2do apellido es NULL      │ 
    │                              │   {r}[d]{lb} {g}→{lb} Cliente que han realizado pedidos.       │  
    │                              │   {r}[e]{lb} {g}→{lb} Comerciales que vendieron a Maria.       │  {r}[?]{lb} {g}→{lb} Consulta Diferente
    │                              │   {r}[f]{lb} {g}→{lb} Crear Vista ResumenPedidos.              │  {r}[>]{lb} {g}→{lb} Menu
    │                              │   {r}[g]{lb} {g}→{lb} Consulta total venta en vista anterior.  │  {r}[!]{lb} {g}→{lb} Salir 
    │                                                                                 │
    ╰─────────────────────────────────────────────────────────────────────────────────╯
    {reset}"""
        self.print_debug(" ",options)

    def choose_option(self: 'Menus') -> None:
        while True:
            choice = input(f'{Fore.BLUE}  {Fore.MAGENTA}{self.pc_user}{Fore.RED}@{Fore.BLUE}DB_SQLpy{Fore.BLACK}~{Fore.GREEN}  {Fore.CYAN}').upper()
            try :
                options = {
                    '1': self.insert_client,
                    '2': self.insert_order,
                    '3': self.insert_commercial,
                    'A': self.list_date_order,
                    'B': self.list_range_order,
                    'C': self.clien_two_lastname_null,
                    'D': self.client_realized_one_order,
                    'E': self.commercial_sales_maria,
                    'F': self.created_view_order,
                    'G': self.total_sales_in_view,
                    '?': self.different_query,
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
    
    def insert_client(self):
        self.print_debug(" ","\n\t\t.:Insertar Cliente:.")
        while True:
            try:
                name = input(f"{Fore.CYAN}Nombre: ").title()
                if name == ">": break
                lastName1 = input("Apellido1: ").title()
                if lastName1 == ">": break
                lastName2 = input("Apellido2 (NULL): ").title()
                if lastName2 == ">": break
                city = input("Ciudad: ").title()
                if city == ">": break
                category = int(input("Categoria: "))
                if category == ">": break
                data = {
                    'name': name,
                    'lastName1': lastName1,
                    'lastName2': lastName2 if lastName2 else None,
                    'city': city,
                    'category': category
                }
                self.db_app.insert_data_client(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def insert_order(self):
        self.print_debug(" ","\n\t\t.:Insertar Pedido:.")
        while True:
            try:
                total = float(input(f"{Fore.CYAN}Total: "))
                if total == ">": break
                date = input("Fecha (yyyy/mm/dd): ")
                if date == ">": break 
                id_client = int(input("ID cliente: "))
                if id_client == ">": break
                id_commercial = int(input("ID Comercial: "))
                if id_commercial == ">": break
                data = {
                    'total': round(total,2),
                    'date': date,
                    'id_client': id_client,
                    'id_commercial': id_commercial
                }
                self.db_app.insert_data_order(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def insert_commercial(self):
        self.print_debug(" ","\n\t\t.:Insertar Commercial:.")
        while True:
            try:
                name = input(f"{Fore.CYAN}Nombre: ").title()
                if name == ">": break
                lastName1 = input("Apellido1: ").title()
                if lastName1 == ">": break
                lastName2 = input("Apellido2: ").title()
                if lastName2 == ">": break
                commission = float(input("Comision: "))
                if commission == ">": break
                data = {
                    'name': name,
                    'lastName1': lastName1,
                    'lastName2': lastName2,
                    'commission': round(commission,2)
                }
                self.db_app.insert_data_commercial(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def list_date_order(self):
        self.db_app.date_order()

    def list_range_order(self):
        self.db_app.range_order()

    def clien_two_lastname_null(self):
        self.db_app.client_two_null()

    def client_realized_one_order(self):
        self.db_app.client_realized_order()

    def commercial_sales_maria(self):
        self.db_app.commercial_sales_to_maria()
    
    def created_view_order(self):
        self.db_app.created_view_order()

    def total_sales_in_view(self):
        self.db_app.total_sales()
    
    def different_query(self):
        self.print_debug(" ","\n\t\t.:Query:.\n")
        while True:
            try:
                query = input(f"{Fore.CYAN}Query (end with ;): ").title()
                if query == ">": break
                self.db_app.different_query(query)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def main_menu(self: 'Menus') -> None:
        os.system("cls" if os.name == 'nt' else "clear")
        self.print_banner()
        self.print_options()
        self.choose_option()
