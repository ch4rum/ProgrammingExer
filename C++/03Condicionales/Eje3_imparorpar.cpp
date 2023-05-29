/* 3. Realice un program que lea un valor entero y determina si se trata de un 
numero par o impar.*/

#include<iostream>

using namespace std;

int main(){
    int number;

    cout<<"Escriba un numero: "; cin>>number;

    if (number == 0){
        cout<<"El numero es 0"<<endl;
    }
    else if (number %2 == 0){
        cout<<"El numero es par "<<endl;
    }
    else {
        cout<<"El numero es impar"<<endl;
    }
    return 0;
}