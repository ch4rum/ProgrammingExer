/* 1. Realice un programa que solicite de la entrada estadar un entero
del 1 al 10 y muestre su tabla de multiplicar*/

#include<iostream>

using namespace std;

int main(){
    int numbers;

    do{
        cout<<"Digite un numero del 1 al 10: "; cin>>numbers;
    }while ((numbers<1) || (numbers>10));

    for (int values =1; values <= 10; values++){
        cout<<numbers<<" * "<<values<<" = "<<numbers*values<<endl;
    }

    return 0;
}