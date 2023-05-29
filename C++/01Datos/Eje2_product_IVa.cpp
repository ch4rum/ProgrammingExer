/*2. Escribe un progrma que de la entrada estándar el precio de un producto y muestre
en la salidad estadar el precio del producto al aplicarle el IVA*/

#include<iostream>

using namespace std;

int main(){
    float price,endPrice, iva;
    cout<<"Digite el precio del producto: "; cin>>price;

    iva = price * 0.21;
    endPrice = price + iva;

    count<<"\nEl precio final al aplicar el IVA es: "<<endPrice<<endl;
    return 0;
}