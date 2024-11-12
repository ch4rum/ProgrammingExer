/* 12. Hacer un menu que considere las siguientes opciones
1. cubo de un numero
2. numero par o impar
3. salir */

#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int options, numbers;

    cout<<"\t"<<endl;
    cout<<"1. Cubo de un numero"<<endl;
    cout<<"2. Numero par o impar"<<endl;
    cout<<"3. Salir"<<endl;
    cout<<"Opcion: "; cin>>options;

    switch(options){
        case 1 :
            cout<<"Digite un numero: "; cin>>numbers;
            numbers = pow(numbers,3);
            cout<<"El cubo es "<<numbers<<endl; break;
        case 2 :
            cout<<"Digite un numero: "; cin>>numbers;
            if (numbers % 2 == 0){
                cout<<"El numero "<<numbers<<" es par"<<endl;
            }
            else {
                cout<<"El numero "<<numbers<<" es impar"<<endl;
            }
            break;
        case 3 :
            cout<<"\n[!] Saliendo ..."<<endl; break;
        default:
            cout<<"No digito ninguna de las opciones"<<endl; break;
    }
    return 0;
}
