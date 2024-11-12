#include <iostream>
#include <cstring>
#include <cctype>

struct Person{
    char name[30];
    int age=0;
    char sexo;
}
personOne;

bool SexoValido(char sexo) {
    return (sexo == 'M' || sexo == 'F');
}

int main(){
    do {
        std::cout<<"Nombre: ";
        std::cin.getline(personOne.name,20,'\n');
        std::cout<<"Edad: ";
        std::cin>>personOne.age;
        std::cin.ignore();
        std::cout<<"Sexo: ";
        std::cin>>personOne.sexo;
        personOne.sexo = std::toupper(personOne.sexo);
        std::cin.ignore();

    }while ((strlen(personOne.name) == 0) || (personOne.age == 0 && std::cin.peek() == '\n') || !SexoValido(personOne.sexo));

    std::printf("\nPersona One\nNombre: %s\nEdad: %d\nSexo: %c\n",personOne.name,personOne.age,personOne.sexo);
    //std::printf("\nPersona Two\nNombre1: %s\nEdad: %d\nSexo: %c\n",personTwo.name,personTwo.age,personTwo.sexo);
    return 0;
}