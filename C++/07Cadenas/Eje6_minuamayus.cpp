/* 6. Convertir dos cadenas de minusculas a Mayusculas. compararlas y decir
si son iguales o no.*/

#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

int main(){
    char phrases[100];
    char phrasesTwo[100];
    int lengthOne, lengthTwo;
    
    do {
        cout<<"Digite la 1ra frase: ";
        cin.getline(phrases,100,'\n');
        lengthOne = strlen(phrases);
    
        cout<<"Digite la 2da frase: ";
        cin.getline(phrasesTwo,100,'\n');
        lengthTwo = strlen(phrasesTwo);

    } while( (lengthOne==0) || (lengthTwo==0) );

    for (int _=0;_<lengthOne;_++){
        phrases[_] = toupper(phrases[_]);
    }
    for (int _=0;_<lengthTwo;_++){
        phrasesTwo[_] = toupper(phrasesTwo[_]);
    }
    if (strcmp(phrases, phrasesTwo) == 0){
        cout<<"Las frases son iguales"<<endl;
    } else {
        cout<<"Las frases no son iguaels"<<endl;
    }

    return 0;
}
