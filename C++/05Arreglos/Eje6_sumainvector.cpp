/* 6. Escribir un programa que defina un vector de numeros y calcule si existe algun
numero en el vector cuyo valor equivale a la suma del resto de numeros
del vector*/

#include<iostream>

using namespace std;

int main(){
    int numbers[5] = {1,2,3,4,5};
    int addition=0, equal=0;

    for(int _=0;_<5;_++){
        addition += numbers[_];
        if (numbers[_] > equal){
            equal = numbers[_];
        }
    }
    if(equal==addition-equal){
        cout<<"El numero "<<equal<<"es la suma de los demas";
    }
    else{
        cout<<"No existe ningun numero que sea la suma de los demas";
    }
    
    return 0;
}