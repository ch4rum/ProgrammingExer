/* 3. Escribe un programa que lea de la entrada un vector de numeros y 
muestre en la salida estandar los numeros del vector con sus indices asociados*/ 

#include<iostream>

using namespace std;

int main(){
    int numbers[100], ninput;

    cout<<"Digite el numero de elementos que va ha tener el arreglo: ";cin>>ninput;
    for(int _=0;_<ninput;_++){
        cout<<"Digite un numero "<<_+1<<" : ";
        cin>>numbers[_];
    }
    for(int _=0;_<ninput;_++){
        cout<<_<<" -> "<<numbers[_]<<endl;
    }
    return 0;
}