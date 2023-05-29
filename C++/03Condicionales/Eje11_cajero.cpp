/* 11. Hacer un programa que simule un cajero automatico con un saldo de
1000 usd.*/

#include<iostream>

using namespace std;

int main(){
    int options;
    float extra, money = 1000;

    cout<<"\t Bienvenido a su Cajero Virtual"<<endl;
    cout<<"1. Ingresar dinero en cuenta\n";
    cout<<"2. Retirar dinero de la cuenta\n";
    cout<<"3. Salir\n";
    cout<<"Opcion:> "; cin>>options;

    switch(options){
        case 1:
            cout<<"Digite la cantidad de dinero a ingresar: "; cin>>extra;
            money += extra;
            cout<<"Dinero en su cuenta: "<<money<<endl; break;
        case 2:
            cout<<"Cuanto dinero va ha retirar: "; cin>>extra;
            if (extra > money){
                cout<<"No tiene esa cantida"<<endl;
            }
            else {
                money -= extra;
                cout<<"Dinero en su cuenta: "<<money<<endl; break;
            }
        case 3:
            cout<<"\n[!] Saliendo ...\n"; break;
        default: 
            cout<<"No digito ninguna de las opciones"<<endl; break;
    }

    return 0;
}