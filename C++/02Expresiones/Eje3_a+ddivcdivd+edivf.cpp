/* 3. Escribe la siguiente Expresion matematicas en c++
(a+(b/c))/(d+(e/f))*/

#include<iostream>

using namespace std;

int main(){
    float a,b,c,d,e,f, result = 0;

    cout<<"Escribe el valor de a: "; cin>>a;
    cout<<"Escribe el valor de b: "; cin>>b;
    cout<<"Escribe el valor de c: "; cin>>c;
    cout<<"Escribe el valor de d: "; cin>>d;
    cout<<"Escribe el valor de e: "; cin>>e;
    cout<<"Escribe el valor de f: "; cin>>f;

    result = (a+(b/c)) / (d+(e/f));

    cout.precision(2);
    cout<<"\nEl resultado es: "<<result<<endl;
    
    return 0;
}