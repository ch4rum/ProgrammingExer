/* 10. Escriba un programa que calcule el valor de: 1!+2!+3!+....n! (suma fact)*/

#include<iostream>

using namespace std;

int main(){
    int factorial = 1, n_number, addition = 0;

    cout<<"Digite el numero: ";cin>>n_number;

    for(int _=1;_<=n_number;_++){
        factorial *= _;
        addition += factorial;
    }
    cout<<"\nLa suma de factoriales es: "<<addition<<endl;
    return 0;
}