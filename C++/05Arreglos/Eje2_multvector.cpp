/* 2. Escribe un programa que defina un vector de numeros y calcule la multiplicacion
acumulada de sus elementos */

#include<iostream>

using namespace std;

int main(){
    int numbers[] = {1,2,3,4,5};
    int multiplication = 1;

    for(int _=0;_<5;_++){
        multiplication *= numbers[_];
    }
    cout<<"\nLa multiuplicacion acumulada es: "<<multiplication<<endl;

    return 0;
}