/* 5. Desarrolle un programa que lea de la entrada un vector de enteros
y determine el mayor elemento del vector.*/

#include<iostream>

using namespace std;

int main(){
    int numbers[100], ninput, greater=0;

    cout<<"Digite el numero de elementos del arreglo: ";cin>>ninput;

    for(int _=0;_<ninput;_++){
        cout<<"Digite un numero "<<_+1<<" : ";
        cin>>numbers[_];

        if (numbers[_] > greater){
            greater = numbers[_];
        }
    }
    cout<<"\nEl mayor numero del vector es: "<<greater<<endl;
    
    return 0;
}