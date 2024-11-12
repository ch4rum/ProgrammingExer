/* 13. Hacer un programa que realize la serie fibonacci -> 1 1 2 3 5 8 13 ... n*/

#include<iostream>

using namespace std;

int main(){
    int n_number, result = 0, previus = 1,next;

    cout<<"Ingrese el valor del numero: ";cin>>n_number;
    cout<<"Los primeros "<<n_number<<" de la serie Fibonacci son: "<<endl;
    
    for (int _=1; _ <= n_number; _++){
        next = result + previus;
        result = previus;
        cout<<result<<" ";
        previus = next;
    }
    return 0;
}