/* 1. Hacer un programa que pida al usuario que digite una cadena de caracteres,
luego verificar la longitud de la cadena, y si esta supera a 10 carcteres
mostrarla en panatalla, caso contrario no mostrarla.*/

#include<iostream>
#include<cstring>

using namespace std;

int main(){

    char phrases[100];
    cout<<"Digite un frase o cadena de caracteres: ";
    cin.getline(phrases,100,'\n');
    int length=strlen(phrases);

    if(length>10){
        cout<<phrases<<endl;
    }

    return 0;
}