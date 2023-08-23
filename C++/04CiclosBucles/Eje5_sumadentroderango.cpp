/* 5. Escriba un programa que lea valores enteros hasta que se 
introdusca un valor en el rango [20-30] o se introduzca el valor 0.
EL programa debe entregar la suma de los valores mayores a 0
introduccidos. */

#include<iostream>

using namespace std;

int main(){
    float number, addition = 0 ;

    do{
        cout<<"Digite un numero: "; cin>>number;
        if (number > 0){
            addition += number;
        }
    }while( ((number<20) || (number>30)) && (number != 0));

    cout<<"\nLa suma es: "<<addition<<endl;
    return 0;
}