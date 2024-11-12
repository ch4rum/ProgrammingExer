/* 7. Escriba un programa que calcule el valor de : 1+2+3...n*/

#include<iostream>

using namespace std;

int main(){
    int n_number, additton = 0;

    cout<<"Digite la cantidad de elementos: ";cin>>n_number;

    for(int _=1;_<=n_number;_++){
        additton += _;
    }
    cout<<"\nLa suma es: "<<additton<<endl;
    return 0;
}