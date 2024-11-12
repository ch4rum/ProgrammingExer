/* 4. Escriba un programa que defina un vector de numeros y muestre
en la salida estandar del vector en orden inverso - del ultimo 
al primer elemento*/

#include<iostream>

using namespace std;

int main(){
    int numbers[] = {1,2,3,4,5};

    for (int _=4;_>=0;_--){
        cout<<numbers[_]<<endl;
    }
    return 0;
}