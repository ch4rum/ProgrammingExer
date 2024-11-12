/* 10. Escriba un progrma que calcule las soluciones de una ecuacion de segundo grado
de la forma ax**2 + bx +c = 0, teniendo en cuenta que :
x= -b+-raizb**2-4ac/2a*/

#include<iostream>
#include<math.h>

using namespace std;

int main(){
    float a,b,c, resultOne = 0, resultTwo = 0;

    cout<<"Digite el valor de a: "; cin>>a;
    cout<<"Digite el valor de b: "; cin>>b;
    cout<<"Digite el valor de c: "; cin>>c;

    resultOne = (-b + sqrt(pow(b,2)-4*a*c))/(2*a);
    resultTwo = (-b - sqrt(pow(b,2)-4*a*c))/(2*a);

    cout.precision(3);
    cout<<"\nEl resultado 1 es: "<<resultOne<<endl;
    cout<<"El resultado 2 es: "<<resultTwo<<endl;
    
    return 0;
}