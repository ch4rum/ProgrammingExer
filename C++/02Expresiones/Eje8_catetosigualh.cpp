/* 8. Escriba un programa que lea de las entradas los dos catetos de u triangulo rectagulo
y escriba en la salida estadar su hipotenusa. */

#include<iostream>
#include<math.h>

using namespace std;

int main(){
    float cat1,cat2,hipotenuse;

    cout<<"Escrina el 1er cateto: "; cin>>cat1;
    cout<<"Escrina el 2do cateto: "; cin>>cat2;

    hipotenuse = sqrt(pow(cat1,2) + pow(cat2,2));

    cout<<"\nLa hipotenusa es: "<<hipotenuse<<endl;

    return 0;
}