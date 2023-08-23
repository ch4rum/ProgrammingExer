/* 3. Realice un programa que calcule y muestre en la salida la suma
de los cudrados de los 10 primeros enteros mayores que 0*/

#include<iostream>

using namespace std;

int main(){
    int addition = 0,  quad;

    for (int values = 0; values <= 10; values++){
        quad = values * values;
        addition += quad;
    }

    cout<<"El resultado de la suma es: "<<addition<<endl;
    return 0;
}