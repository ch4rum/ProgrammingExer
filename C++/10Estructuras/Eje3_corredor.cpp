/*  1. Hacer una estructura llamada corredor , en la cual se tendra los siguientes campos:
Nombre, edad, sexo, club, y pedir datos al usuario para un corredor, y asi una categoria de competicion
- Juvenil <= 18 años
- Señor <= 40 años
- Veterano > 40 años
Posteriormente imprimir todos los datos del corredor, incluida su categoria de competicion.*/

#include <iostream>
#include <cstring>
#include <cctype>
#include <limits>

struct Corredor{
    char name[30];
    int age=0;
    char sexo;
    char club[20];
}personaOne;

int main(){
    char catego[20];

    printf("Nombre: "); std::cin.getline(personaOne.name,30,'\n');
    printf("Edad: "); std::cin>>personaOne.age;
    printf("Sexo: ");std::cin>>personaOne.sexo;
    personaOne.sexo = std::toupper(personaOne.sexo);
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    printf("Club: "); std::cin.getline(personaOne.club,30,'\n');

    if(personaOne.age <= 18){
        strcpy(catego,"Juvenil");
    } else if (personaOne.age <= 40){
        strcpy(catego,"Senior");
    } else {
        strcpy(catego,"Veterano");
    }
    printf("\n\tDatos corredor\n\n");
    printf("Nombre: %s\n",personaOne.name);
    printf("Edad: %d\n",personaOne.age);
    printf("Sexo: %c\n",personaOne.sexo);
    printf("Club: %s\n",personaOne.club);
    printf("Categoria: %s\n",catego);
    return 0;
}