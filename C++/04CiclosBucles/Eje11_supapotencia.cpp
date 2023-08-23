/* 11. Escriba un programa que calcule el valor de: 2¹+2²+2³+....2^n*/

#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int n_number, addition = 0, result = 1;
    
    cout<<"Digite el numero: ";cin>>n_number;

    for (int _=1; _<=n_number;_++){
        //addition += pow(2,_);
        result *= 2;
        addition += result;
    }
    cout<<"\nLa suma de pontecia de 2^n es: "<<addition<<endl;
    return 0;
}