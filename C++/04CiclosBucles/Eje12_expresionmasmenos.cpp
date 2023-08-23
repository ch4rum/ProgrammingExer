/* 12. Hacer un programa que calcule el resultado de la siguiente expresion
1-2+3-4+5-6...n*/

#include<iostream>

using namespace std;

int main(){
    int n_number, addition = 0;

    cout<<"Digite el numero: ";cin>>n_number;

    for (int _=1; _<=n_number;_++){
        if (_%2 == 0){
            addition -= _;
        }
        else {
            addition += _;
        }
    }
    cout<<"\nLa suma es: "<<addition<<endl;
    return 0;
}