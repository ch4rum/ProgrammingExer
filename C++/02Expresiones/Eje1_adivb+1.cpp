/* 1. Escibe la siguiente exprecion en c++ a/b+1*/

#include<iostream>

using namespace std;

int main(){
    float a, b, result = 0;

    cout<<"Digite el valor de a: "; cin>>a;
    cout<<"Digite el valor de b: "; cin>>b;

    result = (a/b)+1;
    
    cout.precision(2);
    cout<<"\nEl resultado es: "<<result<<endl;

    return 0;
}