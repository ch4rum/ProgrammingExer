/* 1. Hacer un programa para rellenar una matriz pidiendo al usuario el numero 
de filas y columnas, posteriormente mostrar la matriz en pantalla.*/

#include<iostream>

using namespace std;

int main(){
    int numbers[100][100], rows, columns;

    cout<<"Digite el numero de filas: "; cin>>rows;
    cout<<"Digite el numero de columnas: "; cin>>columns;

    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            cout<<"Digite un numero ["<<row<<"]["<<column<<"] : ";
            cin>>numbers[row][column];
        }
    }
    cout<<"\nMatriz\n\n";
    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            cout<<numbers[row][column];
        }
        cout<<"\n";
    }
    return 0;
}