/* Escribe un programa que lea la entrada estadar dos numeros y muestre
en la salidad su suma,resta multiplicacion y division*/

#include<iostream>

using namespace std;

int main(){
    int numberOne,numerTwo,addition=0,subtraction=0,multiplication=0,division=0;
    
    cout<<"Digite un numero: "; cin>>numberOne;
    cout<<"Digite otro numero: "; cin>>numerTwo;

    addition = numberOne + numerTwo;
    subtraction = numberOne - numerTwo;
    multiplication = numberOne * numerTwo;
    division = numberOne / numerTwo;

    cout<<"\nLa suma es: "<<addition<<endl;
    cout<<"La Resta es: "<<subtraction<<endl;
    cout<<"La Multiplicacion es: "<<multiplication<<endl;
    cout<<"La Division es: "<<division<<endl;

    return 0;
}