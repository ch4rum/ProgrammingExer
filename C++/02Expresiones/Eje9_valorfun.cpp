/* 9. Realice un programa que calcule el calor que toma la siguiente funcion 
para unos valores dados de x e y f(x,y)=raizx/y**2-1*/

#include<iostream>
#include<math.h>

using namespace std;

int main(){
    float x,y,result = 0;

    cout<<"Dame el valor de x: "; cin>>x;
    cout<<"Dame el valor de y: "; cin>>y;

    result = (sqrt(x))/(pow(y,2)-1);

    cout.precision(3);
    cout<<"\nEl resultado es: "<<result<<endl;

    return 0;
}