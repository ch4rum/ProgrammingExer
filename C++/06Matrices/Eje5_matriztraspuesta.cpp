/* 5. RFealiceun programa que lea una matriz de 3x3 y cree su matriz traspuesta.
La amtriz traspuesta es aquella en la que la columna i era la fila i de la matriz
original
|1 2 3|      |1 4 7|
|4 5 6|  ->  |2 5 8|
|7 8 9|      |3 6 9|*/

#include<iostream>

using namespace std;

int main(){
    int matriz[3][3], numbers;

    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            do{
                cout<<"Digite un numero ["<<rows<<"]["<<columns<<"]: ";
                cin>>numbers;
            }while(numbers<0);
            matriz[rows][columns]=numbers;
        }
    }
    cout<<"\nMatriz Original:"<<endl;
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<matriz[rows][columns]<<" ";
        }
        cout<<"\n";
    }
    cout<<"\nMatriz Traspuesta:\n";
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<matriz[columns][rows]<<" ";
        }
        cout<<"\n";
    }

    return 0;
}