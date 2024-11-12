/* 4. Comprobar si un numero digitado por el usuario es positivo o negativo*/

#include<iostream>

using namespace std;

int main(){
    int number;

    cout<<"Digite un numero: "; cin>>number;

    if (number == 0){
        cout<<"El numero es cero"<<endl;
    }
    else if (number > 0){
        cout<<"El numero es positivo"<<endl;
    }
    else {
        cout<<"El numero es negativo"<<endl;
    }
    return 0;
}