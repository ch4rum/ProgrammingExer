
import os
from algoritmEc import *
from colorama import Fore, Style, init
from prettytable import PrettyTable

class Menus:

    def __init__(self: 'Menus') -> None:
        self.pc_user = os.getlogin()
        self.THIS_VERSION = 1.1
        self.ecuacion = AlgoritmEc()
        self.ecuacionDATA = [0]*(3)

    def print_options(self: 'Menus') -> None:
        options = f"""        
        {Fore.RED}┌─{Fore.LIGHTWHITE_EX} User: {self.pc_user}   
        {Fore.RED}├─ {Fore.LIGHTWHITE_EX}V: {self.THIS_VERSION}   {Fore.RED}┌─────────┐   
        {Fore.RED}└─┬─────────┤ {Fore.LIGHTWHITE_EX}Metodos {Fore.RED}├─────────┐ 
          {Fore.RED}│         └─────────┘         │   
          {Fore.RED}├─ {Fore.LIGHTWHITE_EX}1) Ecuacion cuadratica     {Fore.RED}│
          {Fore.RED}├─ {Fore.LIGHTWHITE_EX}2) Metodo secante          {Fore.RED}│
          {Fore.RED}├─ {Fore.LIGHTWHITE_EX}3) Metodo Newton Raphson   {Fore.RED}│
          {Fore.RED}└─ {Fore.LIGHTWHITE_EX}!) Exit                    {Fore.RED}┘
          """
        print(options)

    def choose_option(self: 'Menus') -> None:
        while True:
            choice = input(f'{Fore.BLUE}  {Fore.MAGENTA}{self.pc_user}{Fore.RED}@{Fore.BLUE}Numerical_methods{Fore.BLACK}~{Fore.GREEN}  {Fore.CYAN}').upper()
            try :
                options = {
                    '1': self.tecnic_cuadratica,
                    '2': self.tecnic_Secante,
                    '3': self.tecnic_newton_raphson,
                    '!': exit
                }
                chosen = options.get(choice)
                if chosen: 
                    chosen()
                else :
                    print(f"\n{Fore.RED}[-] Invalid choice, please try again!{Style.RESET_ALL}\n")
            except Exception as err:
                print(f"\n{Fore.RED}[-] Error: {err}{Style.RESET_ALL}\n") 
    
    def ecuacionDATAf(self: 'Menus') -> None:
        print()
        for count, letter in enumerate("ABC"):
            while True:
                try:
                    self.ecuacionDATA[count] = float(input(f"[+] Datos de A, B y C posicion [{letter}]:> "))
                    break
                except Exception as e:
                    continue

    def tecnic_cuadratica(self: 'Menus') -> None:
            try:
                self.ecuacionDATAf()
                x1, x2 = self.ecuacion.cuadratica(self.ecuacionDATA)
                print(f"\n[+] x1 = {x1}\n[+] x2 = {x2}\n")
            except Exception as e:
                print("\n", e, "\n")
    
    def range_iter(self: 'Menus') -> int:
        print()
        while True:
            try:
                return int(input("[+] Rango maximo ha iterar?:> "))
            except Exception as e:
                continue
            
    def tecnic_Secante(self: 'Menus') -> None:
        try:
            print(f"\n{Fore.GREEN}NOTA: Funcion evaluda en ax² + bx - c{Fore.CYAN}")
            self.ecuacionDATAf()
            range = self.range_iter()
            x = self.ecuacion.tecnic_Secante(self.ecuacionDATA, range)
            table = PrettyTable()
            table.field_names = x[0].keys()
            print()
            for row in x:
                table.add_row([round(values, 6) if isinstance(values, float) else values for values in row.values()])
            print(table)
        except Exception as e:
            print("\n", e, "\n")

    def aprox_init(self: 'Menus') -> tuple[float]:
        print()
        while True:
            try:
                return float(input("[+] Dias aproximacion inicial: ")), float(input("[+] Tolerancia al error: "))
            except Exception as e:
                continue

    def tecnic_newton_raphson(self: 'Menus') -> None:
        try:
            result = self.ecuacion.tecnic_newton_raphson(self.aprox_init(), self.range_iter())
            table = PrettyTable()
            table.field_names = result[0].keys()
            print()
            for row in result:
                table.add_row([round(values, 6) if isinstance(values, float) else values for values in row.values()])
            print(table)
        except Exception as e:
            print("\n", e, "\n")

    def main_menu(self: 'Menus') -> None:
        os.system("cls" if os.name == 'nt' else "clear")
        self.print_options()
        self.choose_option()
