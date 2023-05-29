/* 2. Escribe  la siguiente expresion matematicas como expresion 
a+b / c+d */

#include<iostream>

using namespace std;

int main(){
    float a,b,c,d, result = 0;

    cout<<"Escribe el valor de a: "; cin>>a;
    cout<<"Escribe el valor de b: "; cin>>b;
    cout<<"EScribe el valor de c: "; cin>>c;
    cout<<"Escribe el valor de d: "; cin>>d;

    result = (a+b) / (c+d);
    cout.precision(2);
    cout<<"\nEl resultado es: "<<result<<endl;

    return 0;
}