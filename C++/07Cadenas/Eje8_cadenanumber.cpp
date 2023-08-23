/* 8. Pedir al usuario 2 cadenas de caracteres de numeros, uno entero
y el otro real, convertirlos a sus respectivos valores y despues 
sumarlos,*/

#include <iostream>
#include <cstring>
#include <stdlib.h>

using namespace std;

int main(){
    char numberOne[100], numberTwo[100];
    float numbereal, additions;
    int numberint, lengthOne, lengthTwo;
    bool keyOne = true, keyTwo = true;

    do {
        cout<<"Digite un numero entero: ";cin>>numberOne;
        lengthOne = strlen(numberOne);
        cout<<"Digite un numero real: ";cin>>numberTwo;
        lengthTwo = strlen(numberTwo);
    } while ( (lengthOne==0) || (lengthTwo==0) );
    
    for (int _=0; _<lengthOne;_++){
        if ( (!isdigit(numberOne[_])) ){
            keyOne = false; break;
        }
    }
    for (int _=0; _<lengthTwo;_++){
        if ( (isdigit(numberTwo[_])) ){
            keyTwo = false; break;
        }
    }
    if (keyOne && keyTwo ){
        numberint = atoi(numberOne);
        numbereal = atof(numberTwo);
        additions = numberint + numbereal;
        cout<<"La suma de los 2 numeros es: "<<additions<<endl;
    } else {
        cout<<"Los numeros ingresados no son validos"<<endl;2
    }
    return 0;
}