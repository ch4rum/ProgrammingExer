/* 2. Realice un programa que lea de la entrada estandar numero hasta que se 
introdusca un cero. en ese momento el programa debe terminar y mostrar en la salida
el numero de valores leidos*/

#include<iostream>

using namespace std;

int main(){
    int numbers, count = 0;
    
    do{
       cout<<"Esbriba un numero: "; cin>>numbers;
       if (numbers > 0){
            count ++;
       } 
    }while(numbers != 0);

    cout<<"\nEl total de numeros mayores a 0 es --> "<<count<<endl;

    return 0;
}