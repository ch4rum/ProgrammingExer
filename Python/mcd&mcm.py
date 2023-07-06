#!/bin/python3

__autor__ = "Ch4rum"
__copyright__ = "Copyright © 2023 Ch4rum https://www.instagram.com/ch4rum/"
__version__ = "Version 1.0"
__maintainer__ = "Ch4rum"
__status__ = "Getting better"

import signal, sys, array;

def handler(sig,fram):
    print("\n\n[!] Saliendo...\n");
    sys.exit(1);

# Ctrl + C
signal.signal(signal.SIGINT,handler);

def whole_numbers():
    # Funcion que pide 10 o n cantidad de numeros enteros, valida que sean correctos
    # los datos que se ingresan, se guardan en un array y lo retorna.
    
    numbers = array.array('i'); count = 1;
    print("Puedes calcular n numeros enteros o 10, comenzanzo con almenos 2.\n")
    while True:
        try:
            number = input(f"Ingrese un numero entero {count} [s/S (salir)]: ");
            if number.upper() == "S": break;
            elif int(number) > 0: numbers.append(int(number)); count += 1;
            elif count == 11: break; # <- Si quieres n cantidad de numeros comenta esta linea
        except ValueError:
            print("\nError: debes ingresar un numero entero valido.\n")
    return numbers;

def askMsj(numbers_users):
    # Pregunta si quiere sacar mcd o mcm, validad la respuesta y llama a la 
    # funcion correspondiente.
    
    calculate_mcd = array.array('u');calculate_mcm = array.array('u');
    while True:
        calculate_mcd = input("\nCalcular MCD? [s/N]: ").upper();
        if calculate_mcd == "S":
            if len(numbers_users) == 0:break;
            else:
                mcd_values = mcd(numbers_users);
                print(f"\nEl MCD es: {mcd_values}");
                break;
        elif calculate_mcd == "N": break;
        else:
            print("Error: Ingrese [si/No]");
    while True:
        calculate_mcm = input("\nCalcular MCM? [s/N]: ").upper();
        if calculate_mcm == "S":
            if len(numbers_users) == 0:break;
            else:
                mcm_values = mcm(numbers_users);
                print(f"\nEl MCD es: {mcm_values}");
                break;
        elif calculate_mcd == "N": break;
        else:
            print("Error: Ingrese [si/No]");  

def desFactorial(numbers_users):
    # Saca la descomposicion factorial de un numero y los va guardando en un 
    # diccionario con el numero (llave) y el exponente (valor) n^n.
    
    factorial ={}; x=2;
    while x <= numbers_users:
        if numbers_users % x == 0:
            if x in factorial:
                factorial[x] += 1;
            else:
                factorial[x] = 1;
            numbers_users//=x;
        else:
            x += 1;
    return factorial;

def mcm(numbers_users):
    #  La función calcula el mcm de una lista de n numeros descomponiendo cada 
    # numero (descomposicion factorial), determinando los factores comunes y sus 
    # potencias maximas,luego multiplia estos factores con sus respectivas potencias 
    # para obtener el MCM, retorna el MCM calculado.
    
    lists_fact = {};
    for _ in numbers_users:
        lists2_fact = desFactorial(_);
        for factr,powr in lists2_fact.items():
            if factr in lists_fact:
                lists_fact[factr] = max(lists_fact[factr], powr);
            else:
                lists_fact[factr] = powr;
    mcm = 1;
    for factr,powr in lists_fact.items():
        mcm *= factr**powr;
    return mcm;

def mcd(numbers_users):
    # Esta función recibe una lista de números enteros y calcula su maximo comun divisor. 
    # Utiliza la función 'desFactorial()' para descomponer cada número en factores primos. 
    # Luego, encuentra los factores comunes a todos los números y calcula el MCD multiplicando 
    # los factores comunes elevados a la menor potencia encontrada en los números de la lista. 
    # Retorna el MCD calculado.
    
    lists_fact = desFactorial(numbers_users[0]);
    for _ in numbers_users[1:]:
        lists2_fact = desFactorial(_);
        lists_fact = list(set(lists_fact)&set(lists2_fact));
    mcd = 1;
    for factr in lists_fact:
        #powr = sys.maxsize; 
        #for _ in numbers_users:
        #    fact_powr = desFactorial(_).get(factr,0);
        #    powr = min(powr, fact_powr);
        powr = min([desFactorial(_).get(factr,0) for _ in numbers_users]);
        mcd *= factr ** powr;
    return mcd;

def verify_number_prime(n):
        # Funcion Que Verifica si el numero ingresado es primo o no 
        switch = True ; x = 2;
        while x < n and switch:
            if n % x == 0:
                switch = False;
            x += 1;
        if switch: return True;
        else: return False;

if __name__ == "__main__":
    print("\tMCD & MCM\n");
    numbers_users = whole_numbers();
    askMsj(numbers_users);