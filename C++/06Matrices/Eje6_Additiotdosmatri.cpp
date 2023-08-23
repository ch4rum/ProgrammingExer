/* 6. Realize un programa que calcule la suma de dos matrices cuadradas de 3x3*/

#include<iostream>

using namespace std;


int main(){
    int matrizOne[3][3]={{6,5,1},{4,3,8},{7,2,9}};
    int matrizTwo[3][3]={{7,4,6},{1,5,8},{2,3,9}};

    cout<<"\nMatriz 1:\n";
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<matrizOne[rows][columns]<<" ";
        }
        cout<<"\n";
    }

    cout<<"\nMatriz 2:\n";
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<matrizTwo[rows][columns]<<" ";
        }
        cout<<"\n";
    }
    cout<<"\nSuma de las matrices:\n";
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<matrizOne[rows][columns]+matrizTwo[rows][columns]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}