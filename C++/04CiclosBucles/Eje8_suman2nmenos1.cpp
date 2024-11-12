/* 8. Escriba un programa que calcule el valor de: 1+3+5+...+2n-1*/

#include<iostream>

using namespace std;

int main(){
    int n_number, additton = 0,operation = 0, count = 0;

    cout<<"Digite la cantidad de elementos: ";cin>>n_number;

    for(int _=1;_<=n_number;_+=2){
        additton += _;
        count +=1;
    }
    operation = additton + ((2*count)-1);
    cout<<"\nLa suma es: "<<operation<<endl;
    return 0;
}