/*3. Realice un pograma que lea de la entrada estandar los siguientes datos
de una persona:
    Edad: datos de tipo entero
    Sexo: datos de tipo caracter
    altura en metros: datos de tipo Real
Tras leer los datos, el program debe mostrarlos en la salidad estandar*/

#include<iostream>

using namespace std;

int main(){
    int age; char sex[15]; float height;

    cout<<"Digite su edad: "; cin>>age;
    cout<<"Digite su sexo: "; cin>>sex;
    cout<<"Digite su estatura en metros: "; cin>>height;

    cout<<"\nEdad: "<<age<<endl;
    cout<<"Sexo: "<<sex<<endl;
    cout<<"Estatura: "<<height<<endl;

    return 0;
}