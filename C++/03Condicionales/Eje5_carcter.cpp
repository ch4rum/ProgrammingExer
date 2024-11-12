/* 5. Escriba un programa que lea de la entrada estadar un caracter e indique 
en la salida estadar si el caracter es una vocal minuscula o no */

#include<iostream>

using namespace std;

int main (){
    char letter;

    cout<<"Digite un caracter: "; cin>>letter;

    switch(letter){
        case 'a': 
        case 'e':
        case 'i':
        case 'o':
        case 'u': cout<<"Es una vocal minuscula"<<endl;break;
        default : cout<<"No es una vocal minuscula"<<endl;break;
    }

    return 0;
}