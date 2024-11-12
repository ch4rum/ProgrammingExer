/* 9. Escriba un programa que calcule el valor de: 1*2*3*...*n (factorial)*/

#include<iostream>

using namespace std;

int main(){
    int factorial= 1, n_number;

    cout<<"Digite el numero: ";cin>>n_number;

    for (int _=1;_<=n_number;_++){
        factorial *= _;
    }
    cout<<"\nElfactorial es: "<<factorial<<endl;
    return 0;
}