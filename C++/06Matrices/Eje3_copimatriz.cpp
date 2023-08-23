/* 3. Hacer una matriz de tipo entera 2x2, llenarla de numeros y luego
copiar su contenido hacia otra matriz.*/

#include<iostream>

using namespace std;

int main(){
    int matrizOne[2][2]={{1,2},{3,4}};
    int matrizTwo[2][2];
    
    for(int rows=0;rows<2;rows++){
        for(int columns=0;columns<2;columns++){
            matrizTwo[rows][columns]=matrizOne[rows][columns];
        }
    }
    cout<<"Mostrando matriz 2\n";
    for(int rows=0;rows<2;rows++){
        for(int columns=0;columns<2;columns++){
            cout<<matrizTwo[rows][columns];
        }
        cout<<"\n";
    }


    return 0;
}