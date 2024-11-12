/* 7. Desarrolle un programa que determine si una matriz es simetrica o no. Una 
matriz es sometrica si es cuadrad y si es igual a su matris traspuesta.*/

#include<iostream>

using namespace std;

int main(){
    int matriz[100][100], rows,columns;
    bool flag=false;

    do {
        cout<<"\nDigite cuantas filas: ";cin>>rows;
        if(rows<=0){
            cout<<"\nDigite un numero > 0";
        }
    }while(rows<=0);

    do {
        cout<<"\nDigite cuantas columnas: ";cin>>columns;
        if(columns<=0){
            cout<<"\nDigite un numero > 0";
        }
    }while(columns<=0);

    for(int row=0;row<rows;row++){
        for(int column=0;column<columns;column++){
            cout<<"Digite el numero ["<<row<<"]["<<column<<"]: ";
            cin>>matriz[row][column];
        }
    }
    if(rows==columns){
        for(int row=0;row<rows;row++){
            for(int column=0;column<columns;column++){
                if(matriz[row][column] == matriz[column][row]){
                    flag=true;
                }else{
                    flag=false;
                }
            }
        }
    }
    if(flag){
        cout<<"\nLa matriz es simetrica"<<endl;
    }
    else{
        cout<<"\nLa matriz no es simetrica"<<endl;
    }
    return 0;
}