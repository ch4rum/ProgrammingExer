/* 7. Escriba un programa que solicite una edad(un entero) e
identifique en la salida estandar si la edad introducidad esta
en el rango de 18/25*/

#include<iostream>

using namespace std;

int main(){
    int age;

    cout<<"Digite la edad: "; cin>>age;

    if ((age >= 18) && (age <= 25)){
        cout<<"La edad esta entre el rango de 18/25"<<endl;
    }
    else {
        cout<<"La edad no esta en el rango de 18/25"<<endl;
    }
    return 0;
}