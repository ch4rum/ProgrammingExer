

import os
from colorama import Fore, Style, init  

from Menus.Menu import Menus
from DBs.databaseTwo import DBappTextend
from DBs.conectDB import ConnectDB


class MenuTwo(Menus):

    def __init__(self, db_app):
        super().__init__()
        if not isinstance(db_app, ConnectDB):
            raise ValueError("db_app debe ser una instancia de ConnectDB.")
        self.db_app = DBappTextend(db_app)
        
    def print_optionsTwo(self):
        r = Fore.RED
        g = Fore.GREEN
        lb = Fore.LIGHTBLUE_EX
        reset = Style.RESET_ALL
        options = f"""{lb}
    ╭───────────────────────────────[ Opciones de SQL ]──────────────────────────────╮
    │                                                                                │
    │   {r}[1]{lb} {g}→{lb} Insertar Producto.    │   {r}[a]{lb} {g}→{lb} Calcular total ventas.                 │ {r}[?]{lb} {g}→{lb} Consulta Diferente
    │   {r}[2]{lb} {g}→{lb} Insentar Registro.    │   {r}[b]{lb} {g}→{lb} Obtener stock producto.                │ {r}[>]{lb} {g}→{lb} Menu
    │                               │   {r}[c]{lb} {g}→{lb} Actualizar Stock del producto.         │ {r}[!]{lb} {g}→{lb} Salir 
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    {reset}"""
        self.print_debug(" ",options)

    def choose_optionTwo(self: 'Menus') -> None:
        while True:
            choice = input(f'{Fore.BLUE}  {Fore.MAGENTA}{self.pc_user}{Fore.RED}@{Fore.BLUE}DB_SQLpy{Fore.BLACK}~{Fore.GREEN}  {Fore.CYAN}').upper()
            try :
                options = {
                    '1': self.insert_product,
                    '2': self.insert_registration,
                    'A': self.list_total_sales,
                    'B': self.list_stock_product,
                    'C': self.update_stock_product,
                    '?': self.different_queryDB,
                    '>': self.main_menu_two,
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
    
    def insert_product(self):
        self.print_debug(" ","\n\t\t.:Insertar Producto:.\n")
        while True:
            try:
                name = input(f"{Fore.CYAN}Nombre Producto: ").title()
                if name == ">": break
                priceProduct = input("Precio: ").title()
                if priceProduct == ">": break
                stockProduct = input("Cantidad: ").title()
                if stockProduct == ">": break
                data = {
                    'name': name,
                    'price': priceProduct,
                    'stock': stockProduct
                }
                self.db_app.insert_data_product(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def insert_registration(self):
        self.print_debug(" ","\n\t\t.:Insertar Registro:.")
        while True:
            try:
                id_product = int(input("ID Producto: "))
                if id_product == ">": break
                stock = int(input("Cantidad vendidad: "))
                if stock == ">": break
                data = {
                    'id_product': id_product,
                    'stock': stock
                }
                self.db_app.insert_data_registration(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def list_total_sales(self):
        self.db_app.total_sales()

    def list_stock_product(self):
        self.print_debug(" ","\n\t\t.:Stock del Producto:.\n")
        while True:
            try:
                id_product = int(input("ID Producto: "))
                if id_product == ">": break
                self.db_app.stock_product(id_product)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def update_stock_product(self):
        self.print_debug(" ","\n\t\t.:Update Stock:.\n")
        while True:
            try:
                id_product = int(input("ID Producto: "))
                if id_product == ">": break
                stock = int(input("Cantidad vendidad: "))
                if stock == ">": break
                data = {
                    'id_product': id_product,
                    'stock': stock
                }
                self.db_app.update_stock_product(data)
                break
            except Exception as e:
                self.print_debug("ERROR",e)

    def different_queryDB(self):
        self.print_debug(" ","\n\t\t.:Query:.\n")
        while True:
            try:
                query = input(f"{Fore.CYAN}Query (end with ;): ").strip()
                if query == ">": break
                self.db_app.different_query(query)
                break
            except Exception as e:
                self.print_debug("ERROR",f"ejecutando {e}")

    def main_menu_two(self: 'Menus') -> None:
        os.system("cls" if os.name == 'nt' else "clear")
        self.print_banner()
        self.print_optionsTwo()
        self.choose_optionTwo()
