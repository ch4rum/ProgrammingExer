/* 15. Realice un programa que solicite al usuario un numero entero entre
1 y 100. El programa debe generar un numero aleatorio en ese mismo
rango [1-100], e indicar al usuario si es menor o mayor, hasta 
que lo adivine, por ultimo mostrar el numero de intentos.*/

#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main(){
    int number, ramdon, count = 0;

    srand(time(NULL));
    ramdon = 1 + rand()%(100);

    cout<<"\n\tAdivina el numero"<<endl;

    do{
        cout<<"\nDigite un numero: ";cin>>number;
        
        if (number>ramdon){
            cout<<"\nDigite un numero menor\n";
        }
        if (number<ramdon){
            cout<<"\nDigite un numero mayor\n";
        }
        count ++;
    }while(number != ramdon);

    cout<<"\nFelicidades Adivinastes"<<endl;
    cout<<"Intentos: "<<count<<endl;
    return 0;
}