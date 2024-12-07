#!/bin/python3

import argparse, time, sys, signal

from sortAlgorith import *
from systemarchive import *

def ctrl_c(sig: int, frame: object) -> None:
    """
    Signal manager for the SIGINT signal (Ctrl + C). Exits as failed(1).
    
    Parameters:
    - sig: Signal number.
    - frame: Current execution frame."""

    print(f"\n[{colorama.Fore.LIGHTRED_EX}!{colorama.Style.RESET_ALL}] Saliendo ...\n")
    sys.exit(1)

# Ctrl + C 
signal.signal(signal.SIGINT,ctrl_c)
  
def get_Argument(sort: 'SortAlg') -> argparse.Namespace:
    """
    Gets the arguments passed to the script via the command line.

    Returns:
    - Arguments obtained from the parser."""

    try:
        parse = argparse.ArgumentParser(prog="python Ordenamientos.py",
                                        description="Programa para Analizar algoritmos de ordenamiento")
        parse.add_argument('-b','--bubble',
                           dest='bubble',
                           metavar='</archivo?>',
                           default=None,
                           type=str,
                           help='Pasar archivo con datos para el algoritmo de Burbuja')
        parse.add_argument('-s','--selection',
                           dest='selection',
                           metavar='</archivo?>',
                           default=None,
                           type=str,
                           help='Pasar archivo con datos para el algoritmo de seleccion')
        parse.add_argument('-i','--insertion',
                           dest='insertion',
                           metavar='</archivo?>',
                           default=None,
                           type=str,
                           help='Pasar archivo con datos para el algoritmo de insercion')
        parse.add_argument('-m','--mergesort',
                           dest='mergesort',
                           metavar='</archivo?>',
                           default=None,
                           type=str,
                           help='Pasar archivo con datos para el algoritmo de Mergesort')
        parse.add_argument('-q','--quicksort',
                           dest='quicksort',
                           metavar='</archivo?>',
                           default=None,
                           type=str,
                           help='Pasar archivo con datos para el algoritmo de Quicksort')
        parse.add_argument('-r','--requeriment',
                           dest='requeriment',
                           action='store_true',
                           help='Listar requerimientos.')
        parse.add_argument('-v','--version',
                           action='version',
                           version=f'Ordenamientos.py {sort.__version__.split()[1]}')
        
        if len(sys.argv) == 1 or '-h' in sys.argv:
            sort.banner() 
            print()
            parse.print_help()
            sys.exit(1)
        
        return parse.parse_args()
    except argparse.ArgumentError:
        print("Error de argumentos")
        

def show_msjs(sort_funtion: SortAlg, argsname: str) -> None:
    """
    Displays messages related to data sorting.

    Parameters:
    - sort_function: Sort function to use.
    - argsname: Name of the data file."""

    archives = Archives()
    data = archives.open_archives(argsname)
    if data:
        print(f"{sort_funtion.__doc__}\n")
        p1 = log.progress(f"{colorama.Fore.LIGHTMAGENTA_EX}Ordenando datos{colorama.Style.RESET_ALL}")
        start_time = time.time()
        new_data = sort_funtion(data,p1)
        stop_time = time.time()
        p1.success(f"Tiempo de ejecucion > {colorama.Fore.LIGHTRED_EX}{(stop_time-start_time):.6f}{colorama.Style.RESET_ALL} segundos\n\n")
        #print(new_data)
        archives.export_archive(argsname,new_data)    

if __name__ == "__main__":
    colorama.init()
    sort = SortAlg()
    args = get_Argument(sort)
    sort.banner()
    if args.bubble:
        show_msjs(sort.bubble_sort,args.bubble)
    elif args.selection:
        show_msjs(sort.selection_sort,args.selection)
    elif args.insertion:
        show_msjs(sort.insertion_sort,args.insertion)
    elif args.mergesort:
        show_msjs(sort.mergeSort,args.mergesort)
    elif args.quicksort:
        show_msjs(sort.quickSort,args.quicksort)
    elif args.requeriment:
        listRequeriment = ["pwntools","colorama"]
        [print(f"[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Style.RESET_ALL}] {_}") for _ in listRequeriment]