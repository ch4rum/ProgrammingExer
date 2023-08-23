/* 7. Realiza un programa que defina 2 vectores de caracteres y despues 
almacene el contenido de ambos vectores en un nuevo vector, situando en primer 
lugar los elementos del primer vector seguido por los elementos del segundo
vector. Muestre el contenido del nuevo vector en la salidad estandar.*/

#include<iostream>

using namespace std;

int main(){
    char vetOne[5] = {'a','b','c','d','e'};
    char vetTwo[5] = {'f','g','h','i','j'};
    char vetThree[10];

    for (int _=0;_<5;_++){
        vetThree[_] = vetOne[_];
    }
    for (int _=5;_<10;_++){
        vetThree[_] = vetTwo[_-5];
    }
    cout<<vetThree;endl;
    return 0;
}