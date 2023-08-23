/* 2. Pedir al usuario una cadena de caracteres, almacenarla en un arreglo y
copiar todo su contenido hacia otro arreglo de caracteres.*/

#include<iostream>
#include<cstring>

using namespace std;

int main(){
    char phrases[100];
    char phrasesTwo[100];

    cout<<"Digite una frase o cadena de caracteres: ";
    cin.getline(phrases,100,'\n');

    strcpy(phrasesTwo,phrases);
    cout<<phrasesTwo<<endl;
    return 0;
}