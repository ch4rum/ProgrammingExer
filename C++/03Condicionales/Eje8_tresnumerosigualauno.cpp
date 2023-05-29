/* 8. Escribe un programa que lea de la entrada 3 numeros. Despues debe leer un 
cuarto numero e indicar si el numero coincide con alguno de los introducidos
con anterioridad.*/

#include<iostream>

using namespace std;

in main (){
    int numberOne, numberTwo, numberThree, numberFour;

    cout<<"Dame 3 numeros: "; cin>>numberOne, numberTwo, numberThree;
    cout<<"Dame otro numero: "; cin>>numberFour;

    if ((numberFour == numberOne) || (numberFour == numberTwo) || (numberFour == numberThree)){
        cout<<"El numero coincide con alguno de los introducidos"<<endl;
    }
    else {
        cout<<"El numero no coincide con ninguno"<<endl;
    }
    return 0;
}