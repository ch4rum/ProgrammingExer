/* 4. Escriba un programa que tome cada 4 horas la temperatura exterior,
leyendo durante un periodo de 24 horas. ES decir, debe leer 6 temperaturas.
Calcule la temperatura media del dia, la temperatura mas alta y las mas bja.*/

#include<iostream>

using namespace std;

int main(){
    float temperature, addition_temperature = 0, temperature_medium;
    float temperature_high = 0, temperature_low = 999;

    for(int i=0; i<24;i+=4){
        cout<<"Digite la temperatura a las "<<i<<" horas: "; cin>>temperature;

        addition_temperature += temperature;

        if (temperature > temperature_high){
            temperature_high = temperature;
        }
        if (temperature < temperature_low){
            temperature_low = temperature;
        }
    }
    temperature_medium = addition_temperature / 6;

    cout<<"\nLa temperatura media del dia es: "<<temperature_medium<<"°"<<endl;
    cout<<"La temperatura mas alta es: "<<temperature_high<<"°"<<endl;
    cout<<"La temperatura mas baja es: "<<temperature_low<<"°"<<endl;

    return 0;
}