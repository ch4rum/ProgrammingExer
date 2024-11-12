/* 2. Realiza un programa que defina una matriz de 3x3 y escriba un ciclo
para que muestre la diagonal principal de la matriz.*/

#include<iostream>

using namespace std;

int main(){
    int matriz[3][3]={{1,2,3},{4,5,6,},{7,8,9}};
    cout<<"Matriz completa\n";
    for(int row=0;row<3;row++){
        for(int column=0;column<3;column++){
            cout<<matriz[row][column];
        }
        cout<<"\n";
    }
    cout<<"\nDiagonal principal de la matriz\n";
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            if(rows==columns){
                cout<<matriz[rows][columns]<<endl;
            }
        }
    }

    return 0;
}