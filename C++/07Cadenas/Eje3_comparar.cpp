/* 3. Pedir al usuario que digite 2 cadenas de caracteres, e indicar si ambas
cadenas son iguales, en caso de no serlo, indicar cual es mayor alfabeticamente*/

#include<iostream>
#include<cstring>

using namespace std;

int main(){
    char phrasesOne[100];
    char phrasesTwo[100];
    int lengthOne, lengthTwo;
    
    do {
        cout << "Digite 1ra frase: ";
        cin.getline(phrasesOne, 100, '\n');
        lengthOne = strlen(phrasesOne);
        cout << "Digite 2da frase: ";
        cin.getline(phrasesTwo, 100, '\n');
        lengthTwo = strlen(phrasesTwo);
    } while ((lengthOne == 0) || (lengthTwo == 0)); 

    if(strcmp(phrasesOne,phrasesTwo) == 0){
        cout<<"\nAmbas cadenas son iguales."<<endl;
    }else if(strcmp(phrasesOne,phrasesTwo) < 0){
        cout<<"\nLa mayor albabeticamente es: "<<phrasesOne<<endl;
    }else{
        cout<<"\nLa mayor albabeticamente es: "<<phrasesTwo<<endl;
    }
    return 0;
}