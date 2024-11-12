/* 6. Escribe un programa que calcule x^y, donde tanto como x,y son
enteros positivos, sin utilizar la funcion pow(x,y)*/

#include<iostream>

using namespace std;

int main(){
    int x, y, result = 1, count = 1;

    do{
        cout<<"Digite el valor de x: ";cin>>x;
        cout<<"Digite el valor de la potencia y: ";cin>>y;
    }while((x<0)||(y<0));
    
    /*for (int i=1;i <=y ; i++){
        result *= x;
    }*/
    do{
        result *= x; count ++;
    }while (count <= y);

    cout<<"\nEl resultado es: "<<result<<endl;
    return 0;
}