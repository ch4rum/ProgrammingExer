/* 1. EScriba un programa que lea dos numeros y 
determina cual de ellos es mayor*/

#include<iostream>

using namespace std;

int main(){
    int numberOne, numberTwo;

    cout<<"Digite 2 numeros\n:> "; cin>>numberOne>>numberTwo;

    if (numberOne == numberTwo){
        cout<<"Ambos numeros son iguales"<<endl;
    }
    else if(numberOne > numberTwo){
        cout<<"El mayor es: "<<numberOne<<endl;
    }
    else{
        cout<<"El mayor es: "<<numberTwo<<endl;
    }

    return 0;
}