/* 8. Hacer un programa que lea 5 numeros en un arreglo, los copie 
a otro arreglo multiplicados por 2 y muestre el segundo arreglo.*/

#include<iostream>

using namespace std;

int main(){
    int numbers[5],numberstwo[5];

    for(int _=0;_<5;_++){
        cout<<_+1<<". Digite un numero: ";cin>>numbers[_];
        numberstwo[_]=numbers[_]*2;
    }
    cout<<"\n";
    for(int _=0;_<5;_++){
        cout<<numbers[_]<<" x 2 = "<<numberstwo[_]<<endl;
    }
    return 0;
}