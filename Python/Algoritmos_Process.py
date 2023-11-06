#!/bin/python3

import sys, signal, random, string, os
import colorama as col
from time import sleep

__autor__ = "Ch4rum"
__copyright__ = "Copyright © 2023 Ch4rum https://www.instagram.com/ch4rum/"
__version__ = "Version 1.0"
__maintainer__ = "Ch4rum"

def ctrl_c(sig, frame):
    """
    Manejador de señal para la señal SIGINT (Ctrl + C). Sale como no exitoso(1)
    
    Parámetros:
    - sig: Número de señal.
    - frame: Marco de ejecución actual."""
    print(f"\n\n{col.Fore.RED}[!] Saliendo...{col.Style.RESET_ALL}\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, ctrl_c)

def banner():
    print(f"""{col.Fore.LIGHTRED_EX}
    ________                                      _____                  
    ___  __ \________________________________________(_)_____________ _  
    __  /_/ /_  ___/  __ \  ___/  _ \_  ___/_  ___/_  /__  __ \_  __ `/  
    _  ____/_  /   / /_/ / /__ /  __/(__  )_(__  )_  / _  / / /  /_/ /   
    /_/     /_/    \____/\___/ \___//____/ /____/ /_/  /_/ /_/_\__, /    
                                                              /____/     
    _____________                    ________________                    
    ___    |__  /______ ________________(_)_  /___  /________ ___________
    __  /| |_  /__  __ `/  __ \_  ___/_  /_  __/_  __ \_  __ `__ \_  ___/
    _  ___ |  / _  /_/ // /_/ /  /   _  / / /_ _  / / /  / / / / /(__  ) 
    /_/  |_/_/  _\__, / \____//_/    /_/  \__/ /_/ /_//_/ /_/ /_//____/  
                /____/                                               {col.Style.RESET_ALL}{col.Fore.CYAN}v{__version__.split()[1]}{col.Style.RESET_ALL}""")
    
class TaskProcess:
    """
    Clase que representa un proceso en un sistema operativo. Cada instancia de la clase TaskProcess se utiliza para 
    modelar las características de un proceso específico, incluido su identificador, tiempo de ráfaga, tiempo de llegada, 
    tiempo de espera, tiempo de retorno y tiempo de finalización.

    Atributos:
    - ids: Identificador único del proceso, generado aleatoriamente durante la inicialización.
    - burst: Tiempo de ráfaga del proceso, que representa el tiempo necesario para que el proceso se ejecute en la CPU.
    - arrival: Tiempo de llegada del proceso al sistema, que indica cuándo el proceso entra en la cola de procesos.
    - burst_tmp: Copia del tiempo de ráfaga original del proceso, utilizado para rastrear el tiempo restante de ejecución del proceso.
    - wait_time: Tiempo de espera acumulado del proceso en la cola, calculado como el tiempo transcurrido desde que el proceso entra en la cola hasta que comienza su ejecución.
    - return_: Tiempo de retorno del proceso, definido como el tiempo total que lleva completar un proceso, desde su llegada hasta su finalización.
    - ending: Tiempo de finalización del proceso, que indica cuándo se completa la ejecución del proceso.

    Métodos:
    - randomProcess: Genera una cadena aleatoria que se utiliza como identificador único del proceso.
    - burst_in_memory: Solicita al usuario el tiempo de ráfaga y el tiempo de llegada del proceso y devuelve los valores ingresados."""

    def __init__(self):
        self.ids = self.randomProcess(8)
        self.burst, self.arrival = self.burst_in_memory()
        self.burst_tmp = self.burst
        self.wait_time = 0
        self.return_ = 0
        self.ending = 0

    def randomProcess(self, length):
        abcdNumbers = string.digits + string.ascii_uppercase + string.digits
        randoms = ''.join(random.choice(abcdNumbers) for _ in range (length))
        return randoms

    def burst_in_memory(self):
        while True:
            try:
                print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Proceso: {col.Fore.MAGENTA}{self.ids}{col.Style.RESET_ALL}")
                burst_tmp = int(input(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Ingrese el tiempo del proceso en memoria(rafaga) {col.Fore.MAGENTA}:> {col.Fore.LIGHTWHITE_EX}"))
                arrival = int(input(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Ingrese el tiempo de entrada {col.Fore.MAGENTA}:> {col.Fore.LIGHTWHITE_EX}"))
                return burst_tmp, arrival
            except Exception:
                print(f"{col.Fore.RED}[!] Valor no valido{col.Style.RESET_ALL}")
        
class Cola:
    """
    Clase que representa una cola de procesos en un sistema operativo. La clase Cola se utiliza para gestionar una 
    lista de procesos y ejecutar diferentes algoritmos de planificación, como Round Robin y FIFO.

    Atributos:
    - list_taskProcess: Lista que almacena los procesos presentes en la cola.
    - completed_process: Lista que almacena los procesos que han sido completados.
    - quantum: Valor del quantum utilizado en el algoritmo Round Robin para limitar el tiempo de ejecución de cada proceso.

    Métodos:
    - __init__: Inicializa una nueva instancia de la cola de procesos con listas vacías y un quantum inicializado a cero.
    - quantum_process: Solicita al usuario que ingrese el valor del quantum a utilizar en el algoritmo Round Robin y devuelve el valor ingresado.
    - orderProcessForTime: Ordena la lista de procesos según su tiempo de llegada, asegurándose de que los procesos se ejecuten en el orden correcto.
    - append_taskProcess: Agrega un proceso a la lista de procesos presentes en la cola.
    - run_Round_Robin: Ejecuta el algoritmo Round Robin para los procesos presentes, asignando tiempos de ejecución y cálculos de tiempo de espera y finalización.
    - run_FIFO: Ejecuta el algoritmo FIFO (First In, First Out) para los procesos presentes, gestionando los tiempos de espera y finalización de cada proceso."""
    
    def __init__(self):
        print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Administrando los procesos.{col.Style.RESET_ALL}")
        self.list_taskProcess = []
        self.completed_process = []
        self.quantum = 0
        
    def quantum_process(self):
        while True:
            try:
                quantum_pro = int(input(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Ingrese el Quantum de los procesos {col.Fore.MAGENTA}:> {col.Fore.LIGHTWHITE_EX}"))
                return quantum_pro
            except Exception:
                print(f"{col.Fore.RED}[!] Valor no valido{col.Style.RESET_ALL}")
                
    def append_taskProcess(self, process):
        self.list_taskProcess.append(process)
        print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se ha agregado la tarea {col.Fore.MAGENTA}{process.ids}{col.Style.RESET_ALL}")
    
    def orderProcessForTime(self, list_task):
        for proc in range(1, len(list_task)):
            item = proc
            while (item > 0 and list_task[item].arrival < list_task[item-1].arrival):
                list_task[item], list_task[item-1] = list_task[item-1], list_task[item]
                item = item-1
        return list_task
        
    def run_Round_Robin(self):
        self.quantum = self.quantum_process()
        times = next_procces = 0
        current_execution = None
        self.list_taskProcess = self.orderProcessForTime(self.list_taskProcess)
        mirror_procces = len(self.list_taskProcess)
        flag = True
        
        while (mirror_procces > 0):
            print(f"\n{col.Fore.BLACK}---------- {col.Fore.MAGENTA}{times} {col.Fore.BLACK}----------{col.Style.RESET_ALL}\n")
            if (len(self.list_taskProcess) > next_procces and times >= self.list_taskProcess[next_procces].arrival):
                print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}El proceso {col.Fore.MAGENTA} {self.list_taskProcess[next_procces].ids} {col.Fore.YELLOW}se ingreso a la cola{col.Style.RESET_ALL}")
                self.completed_process.append(self.list_taskProcess[next_procces])
                next_procces += 1
            else:
                if next_procces > 0 or len(self.completed_process) > 0:
                    if (current_execution == None):
                        current_execution = self.completed_process.pop(0)
                        flag = True
                        print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se saca el proceso {col.Fore.MAGENTA}{current_execution.ids} {col.Fore.YELLOW}y se ejecuta{col.Style.RESET_ALL}")
                    
                    if (flag):
                        if (current_execution.burst_tmp >= self.quantum):
                            current_execution.burst_tmp = current_execution.burst_tmp - self.quantum
                            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se resta {col.Fore.MAGENTA}{self.quantum} {col.Fore.YELLOW}a la rafaga del proceso {col.Fore.MAGENTA}{current_execution.ids}{col.Style.RESET_ALL}")
                            times += self.quantum
                            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se aumenta {col.Fore.MAGENTA}{self.quantum} {col.Fore.YELLOW}al tiempo{col.Style.RESET_ALL}")
                        else:
                            times += current_execution.burst_tmp
                            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se aumenta {col.Fore.MAGENTA}{current_execution.burst_tmp} {col.Fore.YELLOW}al tiempo{col.Style.RESET_ALL}")
                            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se resta {col.Fore.MAGENTA}{current_execution.burst_tmp} {col.Fore.YELLOW}a la rafaga de proceso {col.Fore.MAGENTA}{current_execution.ids}{col.Style.RESET_ALL}")
                            current_execution.burst_tmp = 0
                            
                        if (current_execution.burst_tmp < 1):
                            print(f"\n{col.Fore.BLACK}---------- {col.Fore.MAGENTA}{times} {col.Fore.BLACK}----------{col.Style.RESET_ALL}\n")
                            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}El proceso {col.Fore.MAGENTA}{current_execution.ids} {col.Fore.YELLOW}ha finalizado{col.Style.RESET_ALL}")
                            current_execution.ending = times
                            current_execution.return_ = current_execution.ending - current_execution.arrival
                            current_execution.wait_time = current_execution.return_ - current_execution.burst
                            mirror_procces -= 1
                            current_execution = None
                        else:
                            flag = False   
                    else:
                        self.completed_process.append(current_execution)
                        print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Se agrega el proceso {col.Fore.MAGENTA}{current_execution.ids} {col.Fore.YELLOW}que estaba en ejecucion a la cola{col.Style.RESET_ALL}")
                        current_execution = None
                else:
                    times += 1
                    
        print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Resultados:{col.Style.RESET_ALL}\n")
        for task in self.list_taskProcess:
            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Proceso: {col.Fore.MAGENTA}{task.ids}{col.Style.RESET_ALL}")
            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo de retorno : {col.Fore.MAGENTA}{task.return_}{col.Style.RESET_ALL}")
            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo de espera: {col.Fore.MAGENTA}{task.wait_time}{col.Style.RESET_ALL}")
            print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Finalizo: {col.Fore.MAGENTA}{task.ending}{col.Style.RESET_ALL}\n")
        total_return = sum(_.return_ for _ in self.list_taskProcess)
        total_wait = sum(_.wait_time for _ in self.list_taskProcess)
        print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Promedio de retorno: {col.Fore.MAGENTA}{total_return / len(self.list_taskProcess):.3f}{col.Style.RESET_ALL}")
        print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Promedio de espera: {col.Fore.MAGENTA}{total_wait / len(self.list_taskProcess):.3f}{col.Style.RESET_ALL}\n")
           
    def run_FIFO(self):
        first_arrival = None
        times = 0
        self.list_taskProcess = self.orderProcessForTime(self.list_taskProcess)
        while self.list_taskProcess:
            for task in self.list_taskProcess[:]:
                if first_arrival is None:
                    first_arrival = task.arrival
                print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Procesando {col.Fore.MAGENTA}{task.ids}{col.Fore.YELLOW}, con tiempo en memoria {col.Fore.MAGENTA}{task.burst}{col.Style.RESET_ALL}")
                self.completed_process.append(task)
                self.list_taskProcess.remove(task)
                wait_time = max(0, times - task.arrival)
                print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo de espera: {col.Fore.MAGENTA}{wait_time}{col.Style.RESET_ALL}")
                task.wait_time = wait_time
                times = max(times, task.arrival) + task.burst
                task.times_sys_exit = task.wait_time + task.burst
                print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo del sistema: {col.Fore.MAGENTA}{task.times_sys_exit}{col.Style.RESET_ALL}")
                print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tarea Completada.{col.Style.RESET_ALL}")
                
        total_wait = sum(_.wait_time for _ in self.completed_process)
        print(f"\n{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo promedio de espera: {col.Fore.MAGENTA}{total_wait / len(self.completed_process):.3f}{col.Style.RESET_ALL}")
        print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Tiempo total: {col.Fore.MAGENTA}{sum(_.burst for _ in self.completed_process) + first_arrival}{col.Style.RESET_ALL}\n")
        
def main(algoritmo):
    """
    Función principal que controla la lógica principal del programa. La función 'main' se encarga de inicializar los procesos,
    administrar la cola de procesos y ejecutar el algoritmo de planificación especificado (ya sea Round Robin o FIFO).

    Parámetros:
    - algoritmo: Cadena que indica el tipo de algoritmo de planificación a utilizar. Puede ser 'Round_Robin' o 'FIFO'.

    Acciones:
    - Solicita al usuario que ingrese la cantidad de procesos y crea instancias de la clase TaskProcess para cada proceso.
    - Crea una instancia de la clase Cola y agrega los procesos a la cola.
    - Ejecuta el algoritmo de planificación especificado según el valor de 'algoritmo' (Round Robin o FIFO)."""

    print(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Inicializando los Procesos{col.Style.RESET_ALL}\n")
    
    cola_of_taskProcess = []
    for _ in range(int(input(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Ingrese la cantidad de procesos {col.Fore.MAGENTA}:> {col.Fore.LIGHTWHITE_EX}"))):
        procces = TaskProcess()
        cola_of_taskProcess.append(procces)
        
    colaOne = Cola()
    [colaOne.append_taskProcess(_) for _ in cola_of_taskProcess]
    if algoritmo == "Round_Robin":
        colaOne.run_Round_Robin()
    elif algoritmo == "FIFO":
        colaOne.run_FIFO()
       
if __name__ == "__main__":
    col.init()
    if os.name == "nt":
        clearSys = "cls"
    elif os.name == "posix":
        clearSys = "clear"
        
    option = 0
    while (option != 3):
        os.system(clearSys)
        banner()
        try:
            print(F"\n{col.Fore.MAGENTA}1) {col.Fore.YELLOW}Round Robin\n{col.Fore.MAGENTA}2) {col.Fore.YELLOW}FIFO (Firts in first Out)\n{col.Fore.MAGENTA}3) {col.Fore.YELLOW}Exit{col.Style.RESET_ALL}\n")
            option = int(input(f"{col.Fore.LIGHTGREEN_EX}[+] {col.Fore.YELLOW}Ingrese una opcion {col.Fore.MAGENTA}:> {col.Fore.LIGHTWHITE_EX}"))
            if (option == 3):
                print(f"\n{col.Fore.LIGHTGREEN_EX}..Bye!..{col.Style.RESET_ALL}\n")
                sys.exit(0)
            elif (option == 1):
                os.system(clearSys)
                print(f"\n\t{col.Fore.LIGHTBLUE_EX}.: ROUND ROBIN :.{col.Style.RESET_ALL}\n")
                main("Round_Robin")
                sys.exit(0)
            elif (option == 2):
                os.system(clearSys)
                print(f"\n\t{col.Fore.LIGHTBLUE_EX}.: FIFO (Firts in first Out) :.{col.Style.RESET_ALL}\n")
                main("FIFO")
                sys.exit(0)
            else:
                print(f"\n{col.Fore.RED}[-] No selecciono ninguna opcion del menu{col.Style.RESET_ALL}\n")
                input(f"{col.Fore.GREEN}...Pulse enter para Continuar...{col.Style.RESET_ALL}")
        except Exception:
            print(f"\n{col.Fore.RED}[-] Valor no valido! ingresa un entero..{col.Style.RESET_ALL}")
            sleep(1.2)