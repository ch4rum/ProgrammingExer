#!/bin/python3
         
#                         #                        
#                       @@@@#                      
#                     %@@@@@@@                     
#                    @@@@@@@@@@@                   
#                  @@@@@@@@@@@@@@#                
#                @@@@@@@@@@@@@@@@@@.               
#              &@@@@@@@@@@@@@@@@@@@@@              
#            @@@@@@@@@@@@@@@@@@@@@@@@@@            
#           @@/       \@@@@@@@/       \@@          ~ ch4rum
#         @@@@    __   \@@@@@@    _____|@@@        ~ https://github.com/ch4rum/ProgrammingExer
#        @@@@@   |@@|  |@@@@@@   |@@@@@@@@@@       ~ python3
#      %@@@@@@   ---   |@@@@@@      \@@@@@@@@      
#      @@@@@@@    ____/@@@@@@@    __|@@@@@@@@@     
#     .@@@@@@@   |@@@@@@@@@@@@   |@@@@@@@@@@@@     
#      @@@@@@@   |@@@@@ @ @@@@   |@@@@@@@@@@@@     
#       @@@@@@\__|@@@@  @ @@@@\__|@@@@@@@@@@.      
#         @@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@        
#                    @@@@@@@@@@@                   
#                   @@@@@@@@@@@@@                  
#                  @@@@@@@@@@@@@@@                 

import random, signal, sys, os

def handler(sig, frame):
    print(f"\n\n[!] Saliendo ...\n");
    sys.exit(1);

# Ctrl +C
signal.signal(signal.SIGINT, handler);

def generateKey():
    # Genera la contraseña de 4 digitos aleatoria sin repetir decimales
    key = random.sample(range(0,10), 4);
    return key;

def get_picOrFij(key,attempt):
    # Funcion que verifica si es fija o pica; compara en el rango de 4 si esta en la
    # misma posicion es fija o si esta en el numero es pica, retorna picas &  fijas
    picas, fijas = 0, 0;
    for values in range(4):
        if attempt[values] == key[values]: fijas += 1;
        elif attempt[values] in key: picas += 1;
    return picas, fijas;

def showMSJ(count):
    # Muestra un mensaje segun los intentos en que haya adivinado el numero
    if count < 2:
        print(f"* Exelente, eres un maestro estas fuera del alcance de los demas\n");
    elif count < 4:
        print(f"* Muy bueno, puedes ser un gran competidor\n");
    elif count < 8:
        print(f"* Bien, estas progresando debes buscar tus limites\n");
    elif count < 10:
        print(f"* Regular, Aun es largo el camino por recorrer\n");
    else:
        print(f"* Mal, este juego no es para ti\n");

def export(key,count,date_attempt):
    # NewFuncion para exportar el historial de una partida, primero verifica
    # el sistema operativo y si una ruta existe sino la crea, luego abre o crea
    # un nuevo archivo para poner los datos de la partida y guardarlos.
    if os.name == "nt":
        desktop = f"C:\\Users\\{os.getlogin()}\\Desktop\\";
        if not os.path.exists(desktop):
            os.makedirs(desktop);
    elif os.name == "posix":
        desktop = f"/home/{os.getlogin()}/Desktop/";
        if not os.path.exists(desktop):
            os.makedirs(desktop);

    export = open(desktop + "Picas&Fijas.txt", "a");
    export.write(f"\tNueva partida :)\n- Intento: [{count}]\n- Key: {key}\n- Datos intentos: ");
    for values in date_attempt:
        export.write(f"{values}\n");
    export.write("\n\n");
    export.close();
    print(f"Archivo exportado exitosamente! --> {desktop}Picas&Fijas.txt\n");

if __name__ == "__main__":
    print(f"\n\t♠ Picas & Fijas  ♠\n")
    key = generateKey();
    #print(key);
    count = 0; date_attempt = [];
    while count < 12:
        attempt = input("* Ingrese un numero de 4 cifras sin repetir decimales :> ");
        if len(attempt) != 4 or not attempt.isdigit():
            #print(f"Ingrese un numero de 4 cifras sin repetir decimales!");
            continue;
        attempt = [int(values) for values in attempt];
        #for values in attempt:
        #    attempt.append(int(values));
        if len(set(attempt)) < 4:
            #print(f"Ingresa un numero de 4 cifras sin repetir decimales !");
            continue;
        picas , fijas = get_picOrFij(key, attempt);
        count += 1;
        date_attempt.append(attempt);
        print(f"\n- Intento: [{count}]\n- Picas: [{picas}]\n- Fijas: [{fijas}]\n");
        if fijas == 4:
            showMSJ(count);
            break;
        if count == 12:
            showMSJ(count);
            #key_str = "";
            #for values in key:
            #    key_str += str(values);
            print(f"\nLa clave era : {''.join(str(values) for values in key)}\n");
    export(key, count, date_attempt);