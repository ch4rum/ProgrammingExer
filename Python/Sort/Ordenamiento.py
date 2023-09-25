#!/bin/python3
__autor__ = "Ch4rum"
__copyright__ = "Copyright © 2023 Ch4rum https://www.instagram.com/ch4rum/"
__version__ = "Version 1.0"
__maintainer__ = "Ch4rum"

import argparse, time, sys, signal, colorama
from pwn import *

def handler(sig,frame):
    """
    Manejador de señal para la señal SIGINT (Ctrl + C). Sale como no exitoso(1)
    
    Parámetros:
    - sig: Número de señal.
    - frame: Marco de ejecución actual."""

    print(f"\n[{colorama.Fore.LIGHTRED_EX}!{colorama.Style.RESET_ALL}] Saliendo ...\n")
    sys.exit(1)

# Ctrl + C 
signal.signal(signal.SIGINT,handler)

def banner():
    print(f"""{colorama.Fore.GREEN}                                                            
                  :                           tttttttttttttt
           .     t#,                        .E############W,
          ;W    ;##W.   j.                  ...........t#E. 
         f#E   :#L:WE   EW,       GEEEEEEEL           f#f   
       .E#f   .KG  ,#D  E##j      ,;;L#K;;.         .E#i    
      iWW;    EE    ;#f E###D.       t#E           ;WK:     
     L##Lffi f#.     t#iE#jG#W;      t#E          f#D.      
    tLLG##L  :#G     GK E#t t##f     t#E         ,##        
      ,W#i    ;#L   LW. E#t  :K#E:   t#E         ,##        
     j#E.      t#f f#:  E#KDDDD###i  t#E         .K#        
   .D#j         f#D#;   E#f,t#Wi,,,  t#E                   
  ,WK,           G#t    E#t  ;#W:    t#E         :Gi        
  EG.             t     DWi   ,KK:    fE          .j        
  ,                                    :             {colorama.Style.RESET_ALL}{colorama.Fore.BLUE}v{__version__.split()[1]}{colorama.Style.RESET_ALL}""")
    
def get_Argument():
    """
    Obtiene los argumentos pasados al script mediante la línea de comandos.

    Retorna:
    - Argumentos obtenidos del parser."""

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
                           version=f'Ordenamientos.py {__version__.split()[1]}')
        
        if len(sys.argv) == 1:
            parse.print_help()
            sys.exit(1)
        
        return parse.parse_args()
    except argparse.ArgumentError:
        print("Error de argumentos")
        
def open_archives(archive):
    """
    Abre un archivo y lee los datos contenidos en él.

    Parámetros:
    - archive: Nombre del archivo a abrir.

    Retorna:
    - Lista de números enteros leídos desde el archivo."""

    try:
        with open(archive,"r") as file:
            data = file.read().split()
            data = [int(_) for _ in data]
        if not data:
            print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] El archivo esta vacio")
        return data
    
    except FileNotFoundError:
        print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] El archivo no fue encontrado")
    except ValueError:
        print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] Los datos en el archivo no son numeros enteros validos")
        
def bubble_sort(numbers, p1):
    """
    Implementa el algoritmo de ordenación Burbuja,el algoritmo de ordenación Burbuja compara 
    pares de elementos adyacentes en la lista y los intercambia si están en el orden incorrecto.
    Esto se repite hasta que no se requieran más intercambios, lo que indica que la lista está ordenada.

    Complejidad:
    - Peor caso: O(n^2), donde n es el número de elementos en la lista.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - p1: Objeto de registro de progreso.

    Retorna:
    - Lista de números ordenados."""
    for i in range(len(numbers)): #1
        p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}BubbleSort {colorama.Style.RESET_ALL}- Elemento -> [{colorama.Fore.RED}{numbers[i]}{colorama.Style.RESET_ALL}]")
        for j in range(len(numbers)-i-1): #3
            if (numbers[j] > numbers[j+1]): #4
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] #7         
    return numbers # 1

def selection_sort(numbers,p1):
    """
    Implementa el algoritmo de ordenación por Selección.El algoritmo de ordenación por Selección 
    busca el elemento más pequeño en la lista y lo coloca en la posición correcta.
    Esto se repite para todos los elementos de la lista, dividiendo efectivamente la lista en dos 
    partes: la parte ordenada y la parte no ordenada.

    Complejidad:
    - Peor caso: O(n^2), donde n es el número de elementos en la lista.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - p1: Objeto de registro de progreso.

    Retorna:
    - Lista de números ordenados."""
    
    for i in range(len(numbers)):#1
        p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}SelectionSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[i]}{colorama.Style.RESET_ALL}]")
        mini = i #1
        for j in range(i+1,len(numbers)):#2
            if (numbers[j] < numbers[mini]): #3
                mini = j #1
        numbers[i], numbers[mini] = numbers[mini], numbers[i] #5
    return numbers #1

def insertion_sort(numbers,p1):
    """
    Implementa el algoritmo de ordenación por Inserción.El algoritmo de ordenación por Inserción 
    construye una lista ordenada uno a uno, insertando elementos no ordenados en la posición correcta.
    En cada iteración, toma un elemento no ordenado, lo compara con los elementos ordenados y lo 
    inserta en la posición correcta.

    Complejidad:
    - Peor caso: O(n^2), donde n es el número de elementos en la lista.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - p1: Objeto de registro de progreso.

    Retorna:
    - Lista de números ordenados."""
    
    for _ in range(len(numbers)): #1
        p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}InsertionSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[_]}{colorama.Style.RESET_ALL}]")
        pos = _#1
        aux = numbers[_] #2
        while ((pos>0) and (numbers[pos-1] > aux)): #4
            numbers[pos] = numbers[pos-1]#3
            pos -= 1#2
        numbers[pos] = aux#2
    return numbers#1

def mergeSort(numbers,p1):
    """
    Implementa el algoritmo de ordenación Merge Sort. El algoritmo de ordenación Merge Sort utiliza
    la estrategia de "divide y conquista" para dividir la lista en mitades más pequeñas,
    ordenarlas y luego combinarlas en una lista ordenada más grande.

    Complejidad:
    - Peor caso: O(n log n), donde n es el número de elementos en la lista.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - p1: Objeto de registro de progreso.

    Retorna:
    - Lista de números ordenados."""
    
    if len(numbers) > 1:#2
        mid = len(numbers)//2 #3
        L=numbers[:mid]#2
        R=numbers[mid:]#2
        mergeSort(L,p1)
        mergeSort(R,p1)
        i = j = k = 0 #3
        while i<len(L) and j < len(R):#5
            if L[i] <= R[j]: #3
                numbers[k] =L[i]#3
                i += 1#2
            else: 
                numbers[k] = R[j]#3
                j += 1#2
            k += 1#2
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
        while i < len(L):#2
            numbers[k] = L[i]#3
            i +=1 ; k += 1 #4
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
        while j < len(R):#2
            numbers[k] = R[j]#3
            j += 1; k += 1#4
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
    return numbers#1

def quickSort(numbers, p1):
    """
    Implementa el algoritmo de ordenación Quick Sort.El algoritmo de ordenación Quick Sort utiliza
    una estrategia de "divide y conquista" para dividir la lista en sub-listas más pequeñas,
    ordenarlas y combinarlas en una lista ordenada. Utiliza una técnica llamada partición para elegir 
    un elemento como pivote y reorganizar la lista de manera que los elementos menores que el pivote 
    estén a la izquierda y los mayores estén a la derecha.

    Complejidad:
    - Caso promedio y esperado: O(n log n), donde n es el número de elementos en la lista.
    - Peor caso: O(n^2), pero rara vez ocurre en la práctica debido a la elección inteligente de 
    pivotes y las particiones eficientes.
    
    Parámetros:
    - numbers: Lista de números a ordenar.
    - p1: Objeto de registro de progreso.

    Retorna:
    - Lista de números ordenados."""

    def partition(numbers,low,high):
        """
    Función auxiliar para Quick Sort que realiza la partición de la lista.Esta función toma un 
    elemento como pivote (en este caso, el último elemento de la sublista) y reorganiza la lista de 
    manera que los elementos menores que el pivote estén a la izquierda y los mayores estén a la 
    derecha del pivote. Luego, devuelve el índice del pivote después de la partición.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - low: Índice más bajo de la sublista actual.
    - high: Índice más alto de la sublista actual.

    Retorna:
    - Índice del pivote después de la partición."""

        pivot = numbers[high] #2
        i = low - 1 #2
        for _ in range(low,high): #1
            if numbers[_] <= pivot: #2
                i += 1 #2
                numbers[i], numbers[_] = numbers[_], numbers[i] #5
                p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}QuickSort{colorama.Style.RESET_ALL} - Elemento [{colorama.Fore.RED}{numbers[_]}{colorama.Style.RESET_ALL}]")
        numbers[i+1], numbers[high] = numbers[high], numbers[i+1] #5
        return i+1 #2
    
    def quickSortHelp(numbers,low,high):
        """
    Función auxiliar para Quick Sort que implementa la recursión. Esta función es parte del algoritmo 
    Quick Sort y se utiliza para ordenar las sub-listas de manera recursiva. Divide la lista en 
    sub-listas más pequeñas y las ordena llamando a sí misma de manera recursiva en cada sub-lista.

    Parámetros:
    - numbers: Lista de números a ordenar.
    - low: Índice más bajo de la sublista actual.
    - high: Índice más alto de la sublista actual.

    Retorna:
    - Lista de números ordenados en el rango especificado (low - high)."""

        if low < high: #1
            pi = partition(numbers,low,high)
            quickSortHelp(numbers,low,pi-1)
            quickSortHelp(numbers,pi+1,high)
        return numbers
    
    quickSortHelp(numbers,0,len(numbers)-1)
    return numbers

def export_archive(argsname,sort_data):
    """
    Exporta los datos ordenados a un archivo.

    Parámetros:
    - argsname: Nombre del archivo de destino.
    - sort_data: Lista de datos ordenados."""

    with open(argsname,'w') as file:
        file.write('\n'.join(map(str,sort_data))+'\n')
    print(f"[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Style.RESET_ALL}] Archivo exportado exitosamente {colorama.Fore.YELLOW}./{argsname}\n{colorama.Style.RESET_ALL}")    

def show_msjs(sort_funtion,argsname):
    """
    Muestra mensajes relacionados con la ordenación de datos.

    Parámetros:
    - sort_function: Función de ordenación a utilizar.
    - argsname: Nombre del archivo de datos."""

    data = open_archives(argsname)
    if data:
        banner()
        print(f"{sort_funtion.__doc__}\n")
        p1 = log.progress(f"{colorama.Fore.LIGHTMAGENTA_EX}Ordenando datos{colorama.Style.RESET_ALL}")
        start_time = time.time()
        new_data=sort_funtion(data,p1)
        stop_time = time.time()
        p1.success(f"Tiempo de ejecucion > {colorama.Fore.LIGHTRED_EX}{(stop_time-start_time):.6f}{colorama.Style.RESET_ALL} segundos\n\n")
        #print(new_data)
        export_archive(argsname,new_data)    

if __name__ == "__main__":
    colorama.init()
    args = get_Argument()
    if args.bubble:
        show_msjs(bubble_sort,args.bubble)
    elif args.selection:
        show_msjs(selection_sort,args.selection)
    elif args.insertion:
        show_msjs(insertion_sort,args.insertion)
    elif args.mergesort:
        show_msjs(mergeSort,args.mergesort)
    elif args.quicksort:
        show_msjs(quickSort,args.quicksort)
    elif args.requeriment:
        listRequeriment = ["pwntools","colorama"]
        [print(f"[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Style.RESET_ALL}] {_}") for _ in listRequeriment]