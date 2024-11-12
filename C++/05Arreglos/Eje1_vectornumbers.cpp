/* 1. Escriba un programa que defina un vector de numeros y calcule la suma de
sus elementos*/

#include<iostream>

using namespace std;

int main (){
    int numbers[] = {1,2,3,4,5};
    int addition = 0;

    for(int _=0;_<5;_++){
        addition += numbers[_];
    }
    cout<<"\nLa suma de los elementos del vector es: "<<addition<<endl;
    return 0;
}