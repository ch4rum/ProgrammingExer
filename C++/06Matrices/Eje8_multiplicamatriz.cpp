/* 8. Realice un programa que calcule el producto de 2 matrices cuadradad de 3x3*/

#include<iostream>
#include<time.h>

using namespace std;

int main(){
    int matrizOne[3][3], matrizTwo[3][3], product[3][3];

    srand(time(NULL));
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            matrizOne[rows][columns]=1+rand()%(10);
            matrizTwo[rows][columns]=1+rand()%(10);
        }
    }
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            product[rows][columns]=0;
            for(int k=0;k<3;k++){
                product[rows][columns]+=matrizOne[rows][k]*matrizTwo[k][columns];
            }
        }
    }
    cout<<"\nLa multiplicacion de las 2 matrices es: "<<endl;
    for(int rows=0;rows<3;rows++){
        for(int columns=0;columns<3;columns++){
            cout<<product[rows][columns]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}