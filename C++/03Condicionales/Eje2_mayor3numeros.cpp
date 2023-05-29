/* 2. Escriba un progrma que lea 3 numeros y determine cual de ellos es el mayor*/

#include<iostream>

using namespace std;

int main(){
    int numberOne, numberTwo, numberThree;

    cout<<"Escriba 3 numeros\n:> "; cin>>numberOne>>numberTwo>>numberThree;

    if ((numberOne > numberTwo) and (numberOne > numberThree)){
        cout<<"El mator es "<<numberOne<<endl;
    }
    else if((numberTwo > numberOne) && (numberTwo > numberThree)){
        cout<<"El mayor es "<<numberTwo<<endl;
    }
    else{
        cout<<"El mayor es "<<numberThree<<endl;
    }
    return 0;
}