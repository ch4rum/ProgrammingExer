/* 4. Hacer una matriz preguntando al usuario el numeo de filas y columnas,
llenarla de numeros aleatorios,copiar el contenido a otra matriz y por ultimo
mostrarla en pantalla*/

#include<iostream>
#include<time.h>

using namespace std;

int main(){
    int matrizOne[100][100];
    int matrizTwo[100][100], rows, columns;
    
    cout<<"Digite el numero de filas: ";cin>>rows;
    cout<<"Digite el numero de columnas: ";cin>>columns;

    srand(time(NULL));

    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            int random = 1 + rand()%(100);
            matrizOne[row][column]=random;
        }
    }
    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            matrizTwo[row][column]=matrizOne[row][column];
        }
    }
    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            cout<<matrizTwo[row][column]<<" ";
        }
        cout<<"\n";
    }

    return 0;
}