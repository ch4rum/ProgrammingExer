/* 4. Crear una cadena que tenga la siguiente frase "Hola que tal", luego
crear otra cadena para pregunatr al usuario su nombre, por ultimo añadir el
nombre al final de la primera cadena y mostrar el mensaje completo
"Hola que tal (Nombre usuario)"*/

#include<iostream>
#include<cstring>

using namespace std;

int main(){
    char phrases[]="Hola que tal ";
    char nameUser[100];

    cout<<"Cual es tu nombre?: ";
    cin.getline(nameUser,100,'\n');
    strcat(phrases,nameUser);

    cout<<phrases<<endl;

    return 0;
}