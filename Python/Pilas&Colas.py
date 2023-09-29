#!/bin/python3

__autor__ = "Ch4rum"
__copyright__ = "Copyright © 2023 Ch4rum https://www.instagram.com/ch4rum/"
__version__ = "Version 1.0"
__maintainer__ = "Ch4rum"

import sys, signal, os
from time import sleep

def ctrl_c(sig, frame):
    """
    Manejador de señal SIGINT (Ctrl + C) para manejar una salida controlada. Sale como no exitoso (1).
    ---
    Parámetros:
    - sig: Número de señal.
    - frame: Marco de ejecución actual."""

    print(f"\n\n{col.red}[!] {col.reset}{col.blue}Saliendo ...{col.reset}\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT,ctrl_c)

class Colours:
    """Clase para definir código de colores utilizandos en la salida.
    ---
    Atributos:
    - color_codes: Un diccionario que mapea nombre de colores a código ANSI.
    ---
    Metodos:
    - __getattr__: Obtiene el codigo de color correspondiente al nombre especifico."""
    
    color_codes = {
        'green':"\033[38;5;40m",          # Verde
        'dark_green':"\033[38;5;82m",     # Verde Oscuro
        'light_green':"\033[38;5;118m",   # Verde claro
        'reset':"\033[38;0;0m",           # Restablecer a los valores por defecto
        'yellow':"\033[38;5;226m",        # Amarillo
        'light_yellow':"\033[38;5;87m",   # Amarillo claro
        #light_yellow = "\033[38;5;229m"  # Amarillo claro
        'blue':"\033[38;5;27m",           # Azul
        'light_blue':"\033[38;5;39m",     # Azul claro
        'red':"\033[38;5;196m",           # Rojo
        'light_red':"\033[38;5;203m",     # Rojo claro
        'purple':"\033[38;5;165m",        # Púrpura
        'orange':"\033[38;5;208m",        # Naranja
        'pink':"\033[38;5;211m",          # Rosa
        'cyan':"\033[38;5;51m",           # Cian
        'gray':"\033[38;5;240m",          # Gris
        'reset': "\033[0m",               # reset colours
    }

    def __getattr__(self, name):
        if name in self.color_codes:
            return self.color_codes[name]
        else:
            raise AttributeError(f"Color '{name}' not found.")
 
class PilasAndColas:
    """
    Clase para representar pilas y colas y realizar operaciones en ella.
    ---
    Metodos:
    - __init__: Inicializa una estructura con valores y enlace al siguiente elemento.
    ---
    Metodos estaticos:
    - is_valid: Verifica si un elemento es valido(entero) y proporciona un mensaje.
    - created_estructure: Crea una nueva estructura ya sea pila o cola (Inicializar)."""

    #crear
    def __init__(self, values, nextPC=None):
        self.values = values
        self.nextPC = nextPC

    # Is valid
    @staticmethod
    def is_valid(new_element, col):
        try:
            int(new_element)
            return True,f"\n{col.green}[+] {col.reset}{col.blue}Valor ingresado correctamente.{col.reset}\n"
        except:
            return False,f"\n{col.red}[-] {col.reset}{col.blue}Ingrese un numero entero valido.{col.reset}\n"

    # Crear estructura
    @staticmethod
    def created_estructure(methodPC, clearSys, col):
        while True:
            os.system(clearSys)
            print(f"{col.green}[+] {col.reset}{col.blue}Creando la{col.reset} {col.yellow}{methodPC}{col.reset}{col.blue} ...{col.reset}\n")
            values = input(f"{col.green}- {col.reset}{col.blue}Asigne el primer valor {col.reset}{col.cyan}:> {col.reset}")
            is_valid, message = PilasAndColas.is_valid(values,col)
            if is_valid:
                if methodPC == "pila":
                    new_pila = ThePila(int(values))
                elif methodPC == "cola":
                    new_pila = TheCola(int(values))
                print(message)
                sleep(1.2)
                return new_pila
            else:
                print(message)
                sleep(1.2)

class ThePila:
    """
    Clase para representar una pila [LIFO(Last-In-First-Out)] y realizar operaciones en ella.
    ---
    Atributos:
    - numbers_pila: El numero de elementos en la pila (para hacer seguimeiento).
    ---
    Metodos:
    - __init__: Inicializa la pila con el primer elemento especificado.
    - stack: Apila un nuevo elemento en la pila.
    - unstack: Desapila un elemento de la pila.
    - emptyPila: Verifica si la pila esta vacía.
    - printP: Imprime los valores en la pila
    - clearPila: Elimina todos los elementos de la pila."""

    number_pila = 0
    
    def __init__(self, firtPila):
        self.firtPila = PilasAndColas(firtPila)
        self.number_pila += 1
        
    # Apilar
    def stack(self, new_element, col):
        while True:
            is_valid , message = PilasAndColas.is_valid(new_element, col)
            if is_valid:
                self.firtPila = PilasAndColas(int(new_element),self.firtPila)
                self.number_pila += 1
                print(message)
                break
            else:
                print(message)
                new_element = input(f"{col.green}-{col.reset} {col.blue}Valor a agregar {col.reset}{col.cyan}:> {col.reset}")

    #Desapilar
    def unstack(self, col):
        if self.emptyPila():
            print(f"\n{col.orange}[!] {col.reset}{col.blue}No hay nada en la pila.{col.reset}\n")
            return
        self.firtPila = self.firtPila.nextPC
        self.number_pila -= 1
        print(f"\n{col.green}[+] {col.reset}{col.blue}Se ha eliminado un elemento de la pila.{col.reset}\n")

    # Vacia?
    def emptyPila(self):
        return self.number_pila == 0
    
    # Imprimir
    def printP(self, col):
        if self.emptyPila():
            print(f"\n{col.orange}[!] {col.reset}{col.blue}No hay nada en la pila.{col.reset}\n")
            return
        actually = self.firtPila
        print(f"{col.green}[+] {col.reset}{col.blue}Valores en la pila.{col.reset}\n")
        for _ in range(1,self.number_pila+1):
            print(f"{col.green}- {col.reset}{col.blue}Valores ingresados en la pila = {col.reset}{col.yellow}{actually.values}{col.reset}")
            actually = actually.nextPC
        print()
    
    # Borrar pila
    def clearPila(self, col):
        for _ in range(1,self.number_pila + 1):
            print(f"{col.red}[-] {col.reset}{col.blue}Se elimino {col.reset}{col.yellow}{self.firtPila.values}{col.reset}{col.blue} de la pila.{col.reset}")
            self.unstack(col)
        print(f"{col.green}[+] {col.reset}{col.blue}Se borro todos los elementos de la pila.{col.reset}\n")
    
class TheCola:
    """
    Clase para representar una cola [FIFO(Firts-In-Firts-Out)] y realizar operaciones ene ella.
    ---
    Atributos:
    - numbers_cola: El número de elementos en la cola (Para hacer seguimiento).
    ---
    Metodos:
    - __init__: Inizializa una cola con el primer elemento especificado.
    - encolar: Encola un nuevo elemento.
    - desencolar: Desencola un elemento de la cola.
    - emptyCola: Verifica si la cola esta vacia.
    - printC: Imprime los valores en la cola.
    - clearCola: Elimina todos los eleentos de la cola."""

    number_cola = 0
    
    def __init__(self,firtCola):
        self.firtCola = PilasAndColas(firtCola)
        self.lastCola = self.firtCola
        self.number_cola += 1
    
    # Encolar
    def encolar(self, new_element, col):
        while True:
            is_valid, message = PilasAndColas.is_valid(new_element, col)
            if is_valid:   
                new = PilasAndColas(int(new_element))
                if self.emptyCola():
                    self.firtCola = new
                    self.lastCola = new
                else:
                    self.lastCola.nextPC = new
                    self.lastCola = new
                self.number_cola += 1
                print(message)
                break
            else: 
                print(message)
                new_element = input(f"{col.green}-{col.reset} {col.blue}Valor a agregar {col.reset}{col.cyan}:> {col.reset}")
    
    # Desencolar
    def desencolar(self, col):
        if self.emptyCola():
            print(f"\n{col.orange}[!] {col.reset}{col.blue}No hay nada en la cola.{col.reset}\n")
            return
        values = self.firtCola.values
        self.firtCola = self.firtCola.nextPC
        self.number_cola -= 1
        if self.emptyCola():
            self.lastCola = None
        print(f"\n{col.green}[+] {col.reset}{col.blue}Se ha eliminado un elemento de la cola.{col.reset}\n")

    # Vacia?
    def emptyCola(self):
        return self.number_cola == 0

    # Imprimir
    def printC(self, col):
        if self.emptyCola():
            print(f"\n{col.orange}[!]{col.reset} {col.blue}No hay nada en la cola.{col.reset}\n")
            return
        actually = self.firtCola
        print(f"{col.green}[+] {col.reset}{col.blue}Valores en la cola.{col.reset}\n")
        for _ in range(1,self.number_cola+1):
            print(f"{col.green}- {col.reset}{col.blue}Valores ingresados en la cola = {col.reset}{col.yellow}{actually.values}{col.reset}")
            actually = actually.nextPC
        print()
    
    # Borrar Cola
    def clearCola(self, col):
        for _ in range(1,self.number_cola + 1):
            print(f"{col.red}[-] {col.reset}{col.blue}Se elimino {col.reset}{col.yellow}{self.firtCola.values}{col.reset}{col.blue} de la cola{col.reset}")
            self.desencolar(col)
        print(f"{col.green}[+] {col.reset}{col.blue}Se borro todos los elementos de la cola{col.reset}\n")
    
def modify_structure(estructure, emptymetho, X, col):
    """
    Modifica la estructura (pila o cola) eliminando elementos hasta encontrar el valor de X.
    ---
    Parámetros:
    - estructure: La estructura (pila o cola) a modificar.
    - emptymetho: Funcion para verificar si la estructura está vacía.
    - X: El valor que se busca en la estructura.
    - col: Instacia de la clase color para la salida de colores."""
    
    while not emptymetho():
        if isinstance(estructure, ThePila):
            print(f"{col.green}[+] {col.reset}{col.blue}Modificando la Pila.{col.reset}")
            element = int(estructure.firtPila.values)
            if element == X:
                print(f"\n{col.green}[+] {col.reset}{col.blue}Se encontro el valor {col.reset}{col.yellow}{X}{col.reset}\n")
                estructure.printP(col)
                break
            else: 
                estructure.unstack(col)
                print(f"{col.red}[-] {col.reset}{col.blue}Eliminando {col.reset}{col.yellow}{element}{col.reset}{col.blue} elementos.{col.reset}\n")
        elif isinstance(estructure, TheCola):
            print(f"{col.green}[+] {col.reset}{col.blue}Modificando la Cola.{col.reset}")
            element = int(estructure.firtCola.values)
            if element == X:
                print(f"\n{col.green}[+] {col.reset}{col.blue}Se encontro el valor {col.reset}{col.yellow}{X}{col.reset}\n")
                estructure.printC(col)
                break
            else:
                estructure.desencolar(col)
                print(f"{col.red}[-] {col.reset}{col.blue}Eliminando {col.reset}{col.yellow}{element}{col.reset}{col.blue} elementos.{col.reset}\n")
    else:
        print(f"{col.red}[-]{col.reset}{col.blue} No se encontro el valor{col.reset}{col.yellow} {X}{col.reset}{col.blue} en la pila.{col.reset}\n")  

def menuPila(Pila, clearSys, col):
    """
    Muestra un menú de opciones para operar en una pila.
    ---
    Parámentros:
    - Pila: La instancia de la pila en la que se realizarán las operaciones.
    - clearSys: El comando para limpiar la pantalla (segun el OS).
    - col: Instacia de la clase color para la salida de colores."""

    os.system(clearSys)
    try:
        option = int(input(f"""\n\t{col.light_green}.:MENU PILA:.{col.reset}
                           \n{col.purple}1){col.reset} {col.blue}Apilar{col.reset}\n{col.purple}2){col.reset} {col.blue}Desapilar{col.reset}\n{col.purple}3) {col.reset}{col.blue}Esta vacia?{col.reset}\n{col.purple}4) {col.reset}{col.blue}Imprimir Pila{col.reset}\n{col.purple}5) {col.reset}{col.blue}Borrar pila{col.reset}\n{col.purple}6) {col.reset}{col.blue}Modificar estructura{col.reset}\n{col.purple}7) {col.reset}{col.blue}Exit{col.reset}
                           \n{col.green}[+] {col.reset}{col.blue}Ingrese una opcion {col.reset}{col.cyan}:> {col.reset}"""))
        if (option == 1):
            os.system(clearSys)
            print(f"{col.green}[+] {col.reset}{col.blue}Agregando valores a la pila ...{col.reset}\n")
            new_element = input(f"{col.green}-{col.reset} {col.blue}Valor a agregar {col.reset}{col.cyan}:> {col.reset}")
            Pila.stack(new_element, col)
        elif (option == 2):
            os.system(clearSys)
            Pila.unstack(col)
        elif (option == 3):
            os.system(clearSys)
            if Pila.emptyPila():
                print(f"\n{col.orange}[!] {col.reset}{col.blue}No hay ningun elemento en la Pila.{col.reset}\n")
            else:
                print(f"\n{col.green}[+]{col.reset} {col.blue}Hay elementos en la Pila.{col.reset}\n")
        elif (option == 4):
            os.system(clearSys)
            Pila.printP(col)
        elif (option == 5):
            os.system(clearSys)
            Pila.clearPila(col)
        elif (option == 6):
            os.system(clearSys)
            modify_structure(Pila, Pila.emptyPila, 4, col)
        elif (option == 7):
            return Pila
        else:
            print(f"\n{col.red}[-] {col.reset}{col.blue}No selecciono ninguna opcion del menu.{col.reset}\n")

        if input(f"{col.blue}Continuar en el menu? [n/S] {col.reset}{col.cyan}:>{col.reset} ").upper() == "S":
            menuPila(Pila, clearSys, col)
        else:
            return Pila

    except Exception:
        print(f"\n{col.red}[-] {col.reset}{col.blue}Valor no valido, ingrese un numero entero .{col.reset}")
        sleep(1.2)
        menuPila(Pila, clearSys, col)

def menuCola(Cola, clearSys, col):
    """
    Muestra un menú de opciones para operar en una cola.
    ---
    Parámentros:
    - Cola: La instancia de la cola en la que se realizarán las operaciones.
    - clearSys: El comando para limpiar la pantalla (segun el OS).
    - col: Instacia de la clase color para la salida de colores."""
    
    os.system(clearSys)
    try:
        option = int(input(f"""\n\t{col.light_green}.:MENU COLA:.{col.reset}
                           \n{col.purple}1) {col.reset}{col.blue}Encolar{col.reset}\n{col.purple}2){col.reset} {col.blue}Desencolar{col.reset}\n{col.purple}3){col.reset} {col.blue}Esta vacia?{col.reset}\n{col.purple}4){col.reset} {col.blue}Imprimir Cola{col.reset}\n{col.purple}5){col.reset} {col.blue}Borrar Cola{col.reset}\n{col.purple}6){col.reset} {col.blue}Modificar estructura{col.reset}\n{col.purple}7){col.reset} {col.blue}Exit{col.reset}
                           \n{col.green}[+]{col.reset} {col.blue}Ingrese una opcion {col.reset}{col.cyan}:> {col.reset}"""))
        if (option == 1):
            os.system(clearSys)
            print(f"{col.green}[+] {col.reset}{col.blue}Agregando valores a la pila ...{col.reset}\n")
            new_element = input(f"{col.green}-{col.reset} {col.blue}Valor a agregar {col.reset}{col.cyan}:> {col.reset}")
            Cola.encolar(new_element, col)
        elif (option == 2):
            os.system(clearSys)
            Cola.desencolar(col)
        elif (option == 3):
            os.system(clearSys)
            if Cola.emptyCola():
                print(f"\n{col.orange}[!] {col.reset}{col.blue}No hay ningun elemento en la Pila.{col.reset}\n")
            else:
                print(f"\n{col.green}[+]{col.reset} {col.blue}Hay elementos en la Pila.{col.reset}\n")
        elif (option == 4):
            os.system(clearSys)
            Cola.printC(col)
        elif (option == 5):
            os.system(clearSys)
            Cola.clearCola(col)
        elif (option == 6):
            os.system(clearSys)
            modify_structure(Cola, Cola.emptyCola, 7, col)
        elif (option == 7):
            return Cola
        else:
            print(f"\n{col.red}[-] {col.reset}{col.blue}No selecciono ninguna opcion del menu.{col.reset}\n")

        if input(f"{col.blue}Continuar en el menu? [n/S] {col.reset}{col.cyan}:>{col.reset} ").upper() == "S":
            menuCola(Cola, clearSys, col)
        else:
            return Cola

    except Exception:
        print(f"\n{col.red}[-] {col.reset}{col.blue}Valor no valido, ingrese un numero entero .{col.reset}")
        sleep(1.2)
        menuCola(Cola, clearSys, col)
           
def menu(clearSys, col):
    """
    Muestra un menú principal para seleccionar entre crear una pila o una cola.
    ---
    Parámentros:
    - clearSys: El comando para limpiar la pantalla (segun el OS).
    - col: Instacia de la clase color para la salida de colores."""
    
    option = 0
    pila = cola = None
    while (option != 3):
        os.system(clearSys)
        try:
            print(f"\n\t{col.light_green}.:MENU:.{col.reset}\n\n{col.purple}1){col.reset}{col.blue} Crear Pila{col.reset}\n{col.purple}2){col.reset}{col.blue} Crear Cola{col.reset}\n{col.purple}3){col.reset}{col.blue} Exit{col.reset}")
            print(f"\n{col.orange}[!] {col.reset}{col.blue}Primero debes crear una pila o una cola.{col.reset}\n")
            option = int(input(f"{col.green}[+] {col.reset}{col.blue}Ingrese una opcion {col.reset}{col.cyan}:> {col.reset}"))
            if (option == 3):
                print(f"\n{col.blue}..Bye!..{col.reset}\n")
                sys.exit(0)
            elif (option == 1):
                new_pila = PilasAndColas.created_estructure("pila", clearSys, col)
                pila = menuPila(new_pila, clearSys, col)
            elif (option == 2):
                new_cola = PilasAndColas.created_estructure("cola", clearSys, col)
                cola = menuCola(new_cola, clearSys, col)
            else:
                print(f"\n{col.red}[-] {col.reset}{col.blue}No selecciono ninguna opcion del menu{col.reset}\n")
                input(f"{col.blue}...Pulse enter para Continuar...{col.reset}")
        except Exception:
            print(f"\n{col.red}[-] {col.reset}{col.blue}Valor no valido! ingresa un entero..{col.reset}")
            sleep(1.2)
        
if __name__ == "__main__":
    col = Colours()
    if os.name == "nt":
        clearSys = "cls"
        menu(clearSys, col)
    elif os.name == "posix":
        clearSys = "clear"
        menu(clearSys, col)